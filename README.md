# UDP_Sockets

Para ejecutar:

1. Ejecutar el servicio PizarraService.py indicando el puerto 10000:

   ```bash
   $ python3 PizarraService.py 10000
   Escuchando puerto 10000...
   ```

   ![Screenshot from 2020-09-23 18-36-36](/home/charlieromano/Documents/Academico/CESE/Materias/OSApps/TP1_alumnos/UDP_Sockets/Screenshot from 2020-09-23 18-36-36.png)

   ​

2. En otra terminal, ejecutar el cliente main.py:

   ```bash
   $ python3 main.py 
   ```

![Screenshot from 2020-09-23 18-42-00](/home/charlieromano/Documents/Academico/CESE/Materias/OSApps/TP1_alumnos/UDP_Sockets/Screenshot from 2020-09-23 18-42-00.png)



### Manejo de señales

El signal handler eleva una excepción, y con esta tanto el thread principal como el secundario dan un mensaje de "Exit: " terminando el programa.

**Ejemplo excepción capturada por el thread**

```
^CSignal Number: 2  Frame:  <frame at 0x7f472569ca00, file 'main.py', line 46, code start>
  File "main.py", line 76, in <module>
    main()
  File "main.py", line 64, in main
    j1.start()
  File "main.py", line 46, in start
    time.sleep(self.timer)
Exit:Thread

```

**Ejemplo excepción capturada por el main:**

```
^CSignal Number: 2  Frame:  <frame at 0x16c02c0, file 'main.py', line 67, code main>
  File "main.py", line 76, in <module>
    main()
  File "main.py", line 67, in main
    time.sleep(0.5)
Exit: Main
Traceback (most recent call last):
  File "main.py", line 67, in main
    time.sleep(0.5)
  File "/home/charlieromano/Documents/Academico/CESE/Materias/OSApps/TP1_alumnos/UDP_Sockets/mySignals.py", line 10, in myHandler
    raise Exception("Exit service")
Exception: Exit service

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 76, in <module>
    main()
  File "main.py", line 72, in main
    j1.join()
  File "/usr/lib/python3.7/threading.py", line 1039, in join
    raise RuntimeError("cannot join thread before it is started")
RuntimeError: cannot join thread before it is started

```

