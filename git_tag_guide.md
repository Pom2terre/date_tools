# 🏷️ Guide Git Tag - Utilisation complète

## 📌 Lister les tags existants

```bash
git tag
git tag -l | sort -V
```

## 🏷️ Créer un nouveau tag

### ➤ Tag annoté (avec message)
```bash
git tag -a v1.1.0 -m "🎉 Version majeure : nouvelle fonctionnalité"
```

### ➤ Tag léger (sans message)
```bash
git tag v1.1.0
```

## 🚀 Pousser un tag vers GitHub

```bash
git push origin v1.1.0
```

## 🧨 Modifier un tag existant (forcer le tag sur HEAD)

```bash
git tag -f v1.1.0
git push -f origin v1.1.0
```

## ❌ Supprimer un tag

### ➤ Localement
```bash
git tag -d v1.1.0
```

### ➤ Sur le dépôt distant
```bash
git push origin :refs/tags/v1.1.0
```

---

📝 *Dernière mise à jour : générée automatiquement pour impression*