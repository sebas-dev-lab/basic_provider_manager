## Demo

> **Descripción:**      
> - Desarrollado en Python - PostgreSQL
> - Testeado en Linux
> - Funcionamiento básico:
>   - Programa demo básico que permite crear, listar, buscar y exportar en csv a proveedores (guarda nombre, email, teléfono y dirección).
>   - El usuario interactúa por consola mediante opciones.

> **Instalación:**
>   - Prerequisitos:
>       - Instalar PostgeSQL
>       - Python 3.9.2
>       - Linux - Sin testear en windows, en caso de probar en otro SO ignorar los siguientes pasos.
>
>   - Instalación:
>       - Crear tabla provider_contact
         <pre>
                CREATE TABLE IF NOT EXISTS public.provider_contact (
                    id SERIAL PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    phone varchar(50) NOT NULL,
                    email varchar(100) NOT NULL,
                    address varchar(300) NOT NULL
                );
         </pre>


>       - Ejecutar el siguiente comando:

    
> <pre>
>           bash install.sh DB_USER=usuario DB_PASSWORD=contraseña DB_HOST=ip/localhost DB_PORT=puerto DB_NAME=nombre de DB
>       </pre>

>   - Ejecución:
        <pre>
                bash run.sh
        </pre>

