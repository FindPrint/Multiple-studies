```markdown
# 🧊 Déclin de la banquise arctique en septembre (OU + drift quadratique)

Ce dépôt illustre, à l’aide d’un modèle stochastique simple (processus d’Ornstein–Uhlenbeck avec drift quadratique), le déclin accéléré de la banquise arctique en septembre.  
L’objectif est de montrer, de manière reproductible et pédagogique, comment un modèle minimaliste peut capturer l’accélération observée et projeter un Arctique quasi libre de glace en été.

---

## 📊 Résultats principaux

- **Franchissement du seuil critique φ* < 0.5** (Arctique quasi libre de glace en septembre) autour de **2035**.  
- **Fenêtre de franchissement : 2032–2039** selon les trajectoires simulées.  
- Résultat cohérent avec les projections du **GIEC (AR6)** et du **NSIDC**, qui situent la première occurrence entre 2030 et 2050.  

---

## 🔬 Interprétation scientifique

Le franchissement du seuil **φ*(t) < 0.5** en septembre correspond à une situation où l’étendue de la banquise arctique tombe à moins de la moitié de sa valeur climatologique de référence (1981–2010). Autrement dit, l’océan Arctique devient pratiquement libre de glace à la fin de l’été, un état inédit dans l’histoire récente. La médiane des simulations situe ce basculement en **2035**, avec une dispersion entre **2032 et 2039**. Cette fenêtre temporelle traduit à la fois l’accélération du déclin observée depuis les années 2000 et la variabilité stochastique inhérente au système climatique.  

Ce résultat est particulièrement significatif car il s’inscrit dans la fourchette des projections du **GIEC (AR6)** et des analyses du **NSIDC**, qui anticipent la première occurrence d’un Arctique libre de glace en septembre entre 2030 et 2050 selon les scénarios d’émissions. La figure illustre ainsi de manière pédagogique et transparente la convergence entre observations historiques, modélisation stochastique et consensus scientifique international. Elle met en évidence non seulement la tendance centrale (2035), mais aussi l’incertitude et la variabilité, rappelant que l’avenir de la banquise dépend à la fois de la dynamique interne du climat et des trajectoires d’émissions anthropiques.  

---

## 🌍 Version vulgarisée

Chaque année en septembre, la banquise arctique atteint son minimum, après l’été. Les scientifiques suivent cette valeur de près, car elle reflète directement l’impact du réchauffement climatique. Dans notre étude, nous avons utilisé un modèle simple mais robuste pour projeter l’évolution de cette glace de mer.  

Le seuil **φ* < 0.5** signifie que l’étendue de la glace tombe à moins de la moitié de ce qu’elle était en moyenne entre 1981 et 2010. En d’autres termes, l’océan Arctique devient presque libre de glace à la fin de l’été.  

Nos simulations montrent que ce basculement devrait se produire autour de **2035**, avec une marge d’incertitude de quelques années (entre 2032 et 2039). Cela veut dire que, dès la prochaine décennie, nous pourrions voir pour la première fois un océan Arctique quasiment dépourvu de glace en septembre.  

Ce résultat est cohérent avec les prévisions des grands organismes scientifiques comme le **GIEC** ou le **NSIDC**, qui annoncent eux aussi une première occurrence entre 2030 et 2050. La figure que nous présentons est pédagogique : elle montre à la fois la tendance centrale (2035) et la variabilité naturelle du climat. Elle rappelle que, même si l’année exacte reste incertaine, la direction est claire : la glace disparaît rapidement, et cela aura des conséquences majeures pour le climat mondial, les écosystèmes et les sociétés humaines.  

---

## 📂 Structure du dépôt

```
seaice-september-OU/
│
├── code/
│   └── seaice_ou_quadratic.py   # code de simulation et visualisation
│
├── README.md                    # ce fichier
│
└── LICENSE                      # optionnel (ex. MIT)
```

---

## 🚀 Utilisation

1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/<ton-user>/seaice-september-OU.git
   cd seaice-september-OU/code
   ```

2. Lancer le script Python ou notebook pour reproduire les figures.  

---

✍️ *Ce dépôt est volontairement minimaliste : il vise à montrer, de façon transparente et reproductible, comment un modèle simple peut éclairer une question climatique majeure.*
```

---

👉 Veux-tu que je t’aide aussi à transformer ton fichier `.txt` de cellules en un **script Python propre (`seaice_ou_quadratic.py`)** prêt à mettre dans le dossier `code/` ?
