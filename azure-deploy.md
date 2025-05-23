name: Deploy Flask to Azure using Azure CLI

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Nécessaire pour récupérer les tags
      
      - name: 🔄 Fetch full history and tags
        run: |
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          git fetch --prune --tags

      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'  # ← version mise à jour ici

      - name: 📦 Install dependencies
        run: pip install -r requirements.txt

      - name: 🗜️ Create deployment package
        shell: bash
        run: |
          set -e
          mkdir deploy_folder
          shopt -s extglob
          cp -r !(deploy_folder|.git|.github|venv|__pycache__|deploy.zip) deploy_folder/
          cd deploy_folder && zip -r ../deploy.zip . && cd ..

      - name: 🔍 Inspect deploy.zip content
        run: unzip -l deploy.zip

      - name: 🆙 Determine next version
        id: version
        shell: bash
        run: |
          set -e
          git tag --sort=-v:refname
          LATEST=$(git tag --sort=-v:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -n1 || echo "v0.0.0")
          echo "Dernier tag : $LATEST"
          if [[ "$LATEST" =~ ^v([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
            MAJOR="${BASH_REMATCH[1]}"
            MINOR="${BASH_REMATCH[2]}"
            PATCH="${BASH_REMATCH[3]}"
            NEW_VERSION="v${MAJOR}.${MINOR}.$((PATCH + 1))"
          else
            NEW_VERSION="v0.0.1"
          fi
          echo "NEW_VERSION=$NEW_VERSION" >> "$GITHUB_OUTPUT"
          echo "Version calculée : $NEW_VERSION"

      - name: 🏷️ Tag HEAD with NEW_VERSION
        shell: bash
        run: |
          git config user.name "github-actions"
          git config user.email "github-actions@github.com"
          git tag -f ${{ steps.version.outputs.NEW_VERSION }}
          git push -f origin ${{ steps.version.outputs.NEW_VERSION }}

      - name: 🔐 Azure login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: 🕒 Pause avant déploiement pour stabiliser l'environnement
        run: sleep 10

      - name: 🔄 Set APP_VERSION in Azure
        run: |
          az webapp config appsettings set \
            --name date-calc \
            --resource-group RESGrp_Linux \
            --settings APP_VERSION=${{ steps.version.outputs.NEW_VERSION }}

      - name: 🚀 Deploy to Azure Web App
        run: |
          az webapp deploy \
            --name date-calc \
            --resource-group RESGrp_Linux \
            --src-path deploy.zip \
            --type zip

      - name: ✅ Test endpoints
        shell: bash
        run: |
          BASE="https://date-calc.azurewebsites.net"
          sleep 15
          echo "### Résumé des tests" > test-summary.md

          test_url() {
            echo "🔹 Test de $1" >> test-summary.md
            if curl -fsSL "$BASE$1" > /dev/null; then
              echo "✅ $1 OK" >> test-summary.md
            else
              echo "❌ $1 ÉCHEC" >> test-summary.md
            fi
          }

          test_url "/"
          test_url "/hello"
          test_url "/day-of-week"
          test_url "/calculate-duration"

          cat test-summary.md

      - name: 📤 Upload test summary
        uses: actions/upload-artifact@v4
        with:
          name: test-summary
          path: test-summary.md
