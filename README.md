# Ejercicio a) Árbol de decisión
# Hecho por Joaquin Papagianacopoulos

Predecir si un cliente acepta una oferta de plan de datos, usando 10 clientes de ejemplo.

## Cómo correrlo

```
python ejercicio_a.py
```

No necesita instalar nada.

## Qué hace el código

1. Calcula la **entropía** del conjunto original: 5 "Sí" y 5 "No", entonces vale **1.0**.
2. Agrupa Edad y Uso de datos en rangos y calcula la **ganancia de información** de cada atributo.
3. Arma el árbol con el mejor atributo.

## Resultados

| Atributo | Ganancia |
|---|---|
| Edad | 0.449 |
| Uso de datos | 0.600 |
| **Tiene línea fija** | **1.000** |

## Árbol final

```
Tiene línea fija?
├── Sí -> Acepta la oferta
└── No -> No acepta la oferta
```

## Conclusión

**Tiene línea fija** es el mejor atributo para empezar el árbol. Separa perfectamente a los clientes que aceptan de los que no, así que no hace falta seguir dividiendo.
