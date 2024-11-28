Se encuentra en la carpeta PROYECTVENV, 2 codigos que ocupan se necesitan correr

- methods_dbs; Hace correr la FASTAPI.
- listen_sensores; Escucha datos de sensores por medio de MQTT, para subirlos a la base de datos.

Ademas estan otros dos que solitos van a ser llamados por otros codigos

- dbs; Inicializa estructuras para poder interactuar con la base de datos.
- post_to_mysql; Manda a llamar POST de la FASTAPI para subir datos a MYSQL

Se encuentra en la carpeta webpage, el codigo de react.

- Se corre utilizando (npm run dev)
- Lo que programamos se encuentra /webpage/app/page.tsx y /webpage/app/globals.css

Se encuentra en la carpeta Carrito, todo codigo que es corrido en el carrito.

- motores; maneja la logica de los motores.
- publish_MQTT; Ciclo principal que va a estar corriendo en el Carrito 
    (Envio de datos y Escuchando instrucciones para mover el carrito)
- send_data; que es utilizada para enviar datos a MQTT