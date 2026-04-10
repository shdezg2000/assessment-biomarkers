# Assessment: Clasificación de Biomarcadores para Alzheimer

## Descripción

Este repositorio contiene un assessment técnico para evaluar habilidades de Machine Learning aplicadas a datos biomédicos. El reto consiste en construir un clasificador para distinguir entre tres etapas cognitivas usando biomarcadores del framework **AT(N)** (Amyloid, Tau, Neurodegeneration):

- **NC** — Normal Cognition
- **MCI** — Mild Cognitive Impairment  
- **AD** — Alzheimer's Disease

> Disclaimer: El dataset es **sintético** y no contiene datos reales de pacientes. Fue diseñado con fines educativos.

---

## Estructura del repositorio

```
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias de Python
├── data/
│   ├── biomarker_data.csv             # Dataset sintético (485 muestras)
│   └── generate_dataset.py            # Script de generación (referencia)
├── notebooks/
│   └── assessment.ipynb               # ← Notebook que debes completar
```

---

## Instrucciones

### 1. Haz fork de este repositorio

Haz click en **Fork** en la esquina superior derecha de GitHub.

### 2. Clona tu fork

```bash
git clone https://github.com/TU_USUARIO/alzheimer-ml-assessment.git
cd alzheimer-ml-assessment
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Completa el notebook

Abre `notebooks/assessment.ipynb` en Jupyter y completa las tres partes:

| Parte | Tema | Peso |
|---|---|---|
| **Parte 1** | Exploración de datos | 30% |
| **Parte 2** | Modelado y mejora del baseline | 40% |
| **Parte 3** | Análisis crítico e interpretación | 30% |

### 5. Envía tu trabajo

```bash
git add .
git commit -m "Assessment completado"
git push origin main
```

Envía la **liga de tu fork** a Angel Peña (6271506213).

---

## Reglas

- **Puedes usar:** documentación, Google, Stack Overflow, libros.
- **Evita usar** ChatGPT, Claude, u otros LLMs para generar el código completo. Preferimos ver **tu razonamiento** :)) .
- Puedes instalar librerías adicionales si lo justificas.
- Tu notebook debe correr de principio a fin sin errores.

---

## Requisitos del sistema

- Python 3.8+
- Jupyter Notebook o JupyterLab
- Las dependencias listadas en `requirements.txt`

---

## Contexto del proyecto

Este assessment es parte del proceso de selección para un equipo de investigación enfocado en el desarrollo de **modelos predictivos de Alzheimer a través de biomarcadores**, usando datos del framework AT(N) y técnicas de Machine Learning.

El dataset simula la estructura de datos provenientes de la base **ADNI** (Alzheimer's Disease Neuroimaging Initiative), con biomarcadores de líquido cefalorraquídeo (CSF) y sangre (plasma).

---

## ¿Preguntas?

Si tienes dudas sobre las instrucciones, envía un mensaje al equipo evaluador.