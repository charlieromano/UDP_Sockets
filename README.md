# UDP_Sockets

Para ejecutar:

1. Ejecutar el servicio PizarraService.py indicando el puerto 10000:

   ```bash
   $ python3 PizarraService.py 10000
   Escuchando puerto 10000...
   ```

   ![Screenshot from 2020-09-23 18-36-36](/home/charlieromano/Documents/Academico/CESE/Materias/OSApps/TP1_alumnos/UDP_Sockets/Screenshot from 2020-09-23 18-36-36.png)
<img src="./Screenshot%20from%202020-09-23%2018-36-36.png">
   

2. En otra terminal, ejecutar el cliente main.py:

   ```bash
   $ python3 main.py 
   ```

![Screenshot from 2020-09-23 18-42-00](/home/charlieromano/Documents/Academico/CESE/Materias/OSApps/TP1_alumnos/UDP_Sockets/Screenshot from 2020-09-23 18-42-00.png)
<img src="./Screenshot%20from%202020-09-23%2018-36-36.png">



### Manejo de señales

El signal handler eleva una excepción, y con esta tanto el thread principal como el secundario dan un mensaje de "Exit: " terminando el programa.

**Ejemplo excepción **

```
^CSignal Number: 2  Frame:  <frame at 0x18eb2c0, file 'main.py', line 67, code main>
  File "main.py", line 77, in <module>
    main()
  File "main.py", line 67, in main
    time.sleep(0.5)
Exit: Main
Exit:Thread
```
<img src="./Screenshot%20from%202020-10-01%2019-58-40.png">
