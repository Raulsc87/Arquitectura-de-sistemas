# Arquitectura de Sistemas

Repositorio utilizado para guardar las tareas y proyectos del curso.

## Información del estudiante

- Nombre: Raúl Soto
- Carrera: Ingeniería en Sistemas
- Universidad: Universidad Mesoamericana
- Curso: Arquitectura de Sistemas
- Sección: D
- Carné: 202308084


## Tarea 04: página estática con Vite, S3 y CloudFront

La página Nexo presenta usuarios, clientes, productos, ventas y proveedores. Está escrita en HTML, CSS y JavaScript, es responsive y funciona sin iniciar Django. No realiza solicitudes a la API.

### Ramas y API anterior

Esta rama `hw-04` se creó desde `main` (5add9a8). `main` solo contenía este README. La API anterior permanece en `hw-03` (6584177); no se copiaron ni modificaron sus archivos.

Se revisaron `config/settings.py`, `config/urls.py` y `requirements.txt` en `hw-03`: existen las cinco aplicaciones, JWTAuthentication, IsAuthenticated y las rutas `/api/token/`, `/api/token/refresh/` y `/api/token/verify/`. No hay una configuración `SIMPLE_JWT` que establezca 30 minutos y un día, por lo que esas duraciones del contexto no quedan confirmadas. Esta práctica no modifica la autenticación.

Para consultar la documentación original de Django, abrir [README de hw-03](https://github.com/Raulsc87/Arquitectura-de-sistemas/blob/hw-03/README.md). Para ejecutar la API, usar un checkout separado de `hw-03`, crear un entorno virtual, instalar su `requirements.txt`, ejecutar `python manage.py migrate`, `python manage.py createsuperuser` y `python manage.py runserver`. Sus dependencias y rutas siguen conservadas en esa rama. El despliegue del backend queda fuera del alcance.

### Instalar y probar la página

Requisito: Node.js 24 y npm. Desde la raíz del repositorio:

```sh
cd frontend
npm ci
npm run dev
npm run build
npm run preview
```

En PowerShell, si `npm.ps1` está bloqueado, utilizar `npm.cmd` en los mismos comandos. Abrir la dirección que indique Vite. El build genera `frontend/dist/index.html` y sus recursos. `preview` sirve el build local; no publica en AWS.

### Pipeline

`.github/workflows/deploy.yml` se activa con push a `hw-04` y permite ejecución manual. El despliegue solo se permite desde esa rama. Para que aparezca el botón manual, GitHub requiere que el workflow también esté en la rama predeterminada; inicialmente se puede usar el evento push a `hw-04`.

1. **Build:** instala con `npm ci` y genera `dist/` con Vite.
2. **Upload:** obtiene credenciales temporales con OIDC y sincroniza `frontend/dist/` con S3.
3. **Invalidate:** tras una subida exitosa solicita a CloudFront invalidar `/*`.

La concurrencia comparte un grupo único y no cancela despliegues en curso. GitHub puede reemplazar ejecuciones pendientes por una más reciente; se publica la versión pendiente más nueva después de completar la actual. No se promete una ejecución por cada push.

**El bucket debe estar dedicado a esta página:** `aws s3 sync --delete` elimina los objetos que no existen en `dist/`. No guardar allí archivos de Django, documentos ni otras aplicaciones. Una subida no es atómica; comprobar el sitio después de cada despliegue. El paso Invalidate confirma la solicitud; la propagación de la invalidación puede tardar unos minutos.

### Configurar AWS manualmente

Los JSON de `docs/aws/` son plantillas. Sustituir `ACCOUNT_ID`, `BUCKET` y `DISTRIBUTION_ID` por valores de tu cuenta antes de pegarlos en AWS. No contienen credenciales.

1. En S3, crear un bucket de propósito general exclusivo para la página. Elegir región y nombre único; conservar Block all public access, Object Ownership: Bucket owner enforced y cifrado SSE-S3. No activar alojamiento web estático.
2. En CloudFront, crear manualmente una distribución con el bucket S3 como origen, usando su endpoint normal de S3, no un endpoint de website. Dejar Origin path vacío. Elegir Origin Access Control (OAC), crear el control y seleccionar Sign requests (always).
3. Configurar Viewer protocol policy: Redirect HTTP to HTTPS, métodos GET/HEAD y Default root object: `index.html` (sin `/`). El dominio predeterminado de CloudFront basta para esta práctica. Esperar a que la distribución termine de desplegarse.
4. Copiar el ID y dominio de la distribución. En S3 → Permissions → Bucket policy, aplicar `docs/aws/s3-cloudfront-policy.json` con tus valores. Permite lectura solo a esa distribución mediante OAC; mantener el bucket privado.
5. En IAM → Identity providers, agregar OpenID Connect con URL `https://token.actions.githubusercontent.com` y Audience `sts.amazonaws.com`. Si ya existe, reutilizarlo.
6. Crear un rol IAM para identidad web. Aplicar la confianza de `docs/aws/github-trust-policy.json`, con tu cuenta. Restringe el acceso al repositorio `Raulsc87/Arquitectura-de-sistemas` y a `hw-04`. No agregar un GitHub Environment al job sin adaptar la confianza, porque cambia el claim `sub`.
7. Adjuntar al rol una política propia basada en `docs/aws/github-permissions-policy.json`. Solo permite listar, subir y eliminar en el bucket elegido, e invalidar la distribución elegida. No adjuntar AdministratorAccess. Copiar el ARN del rol.
8. En GitHub → Settings → Secrets and variables → Actions → Variables, crear las cuatro variables siguientes. Son variables de repositorio; no hacen falta claves AWS permanentes.

| Variable | Valor que debes colocar |
| --- | --- |
| `AWS_REGION` | Región real del bucket |
| `S3_BUCKET` | Nombre del bucket, sin `s3://` |
| `CLOUDFRONT_DISTRIBUTION_ID` | ID de la distribución, no su dominio |
| `AWS_ROLE_ARN` | ARN completo del rol OIDC |

No compartir contraseñas, tokens, claves de acceso ni claves privadas en el chat. Para continuar solo necesitamos la región, nombre del bucket, ID de distribución, ARN del rol y dominio público de CloudFront.

### Publicar y reunir evidencias

No se ha hecho push. Cuando autorices publicarlo y las variables estén configuradas, el siguiente comando desde esta rama activará el pipeline:

```sh
git push -u origin hw-04
```

Después, revisar Actions y abrir `https://` seguido del dominio real de tu distribución. Comprobar la página, estilos, módulos y presentación móvil. Verificar que HTTP redirige a HTTPS. Si aparece 403, revisar OAC, bucket policy y `index.html`; si aparece una versión antigua, esperar a que termine la invalidación y recargar.

- URL real de CloudFront: **pendiente**.
- Última ejecución exitosa y enlace a su run: **pendientes**.
- Captura pública: **pendiente**, guardar `docs/capturas/pagina-cloudfront.png`.
- Captura del pipeline exitoso: **pendiente**, guardar `docs/capturas/github-actions-exitoso.png`.

Agregar aquí la URL real, el enlace a la última ejecución exitosa e insertar las capturas cuando existan. La práctica no está terminada hasta comprobar ambos resultados. No se han creado recursos en tu cuenta AWS.

### Referencias oficiales

- [Vite: requisitos y comandos](https://vite.dev/guide/)
- [Checkout v6](https://github.com/actions/checkout)
- [Setup Node v7](https://github.com/actions/setup-node)
- [Configure AWS credentials v6](https://github.com/aws-actions/configure-aws-credentials)
- [OIDC con AWS en GitHub](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws)
- [CloudFront: acceso privado a S3 mediante OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
