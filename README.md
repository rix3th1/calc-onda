# Calculadora Gráfica de Longitud de Onda

Este es un pequeño programa que calcula y grafica la longitud de onda de un objeto en movimiento.

## Requisitos

Para ejecutar este programa, necesitarás instalar algunos paquetes adicionales. Puedes hacerlo utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar este programa, simplemente ejecuta el siguiente comando:

```bash
python main.py
```

La aplicación se abrirá en una ventana tkinter y te mostrará un cuadro de diálogo donde podrás ingresar los valores de frecuencia, velocidad y amplitud del objeto en movimiento. Una vez que hayas ingresado estos valores, el programa calculará la longitud de onda y graficará la onda en la ventana tkinter.

## Compilación

Para compilar este programa, puedes utilizar el siguiente comando:

```bash
pyinstaller --onefile --windowed main.py --name calc-onda
```

Esto creará un archivo llamado `calc-onda.exe` que puedes ejecutar en tu sistema operativo.

## Autor

Este programa fue creado por [Ricardo Rojas](https://github.com/rojasricor) y se ha publicado bajo la licencia MIT.
