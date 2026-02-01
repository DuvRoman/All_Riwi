# 🍔 ComaPues - Sistema de Gestión Gastronómica

¡Bienvenido a **ComaPues**! Una solución integral para la gestión de pedidos de comida rápida, diseñada para ser rápida, intuitiva y modular.

---

## 📝 Descripción del Sistema
**ComaPues** es una *Single Page Application* (SPA) que simula la experiencia completa de un restaurante digital. Desde que el usuario se antoja de una hamburguesa hasta que el administrador marca el pedido como "Entregado".

**Tecnologías utilizadas:**
* **Vite.js:** Entorno de desarrollo ultra rápido.
* **JavaScript (ES6+):** Lógica modular y limpia.
* **JSON-Server:** API REST simulada para persistencia de datos.
* **CSS3:** Diseño responsivo con arquitectura de componentes.

---

## 👥 Roles del Sistema

El sistema cuenta con un control de acceso basado en roles para mantener la seguridad y el orden:

| Icono | Rol | Funciones Principales |
| :---: | :--- | :--- |
| 👤 | **Usuario** | Ver menú, filtrar productos, gestionar carrito, actualizar perfil y ver sus pedidos. |
| 👑 | **Administrador** | Gestionar estados de pedidos (PATCH), promover usuarios a Admin y control total de ventas. |

---

## 🔄 Flujo de Uso

1.  **Ingreso:** El usuario se registra o inicia sesión (los datos se validan contra el servidor).
2.  **Pedido:** Navega por el menú, añade productos al carrito y confirma su compra.
3 **Registro de Orden:** Al confirmar, se genera un objeto `pedido` en la base de datos vinculado al ID del usuario.
4.  **Gestión:** El administrador recibe la notificación en su panel y actualiza el progreso (Ej: de *Pendiente* a *En Camino*).
5.  **Perfil:** El usuario puede actualizar su información personal en cualquier momento.

---

## 🚀 Cómo Ejecutar el Proyecto

Sigue estos pasos para tener el sistema corriendo en tu máquina local:

### 1. Clonar y Preparar
```bash`
# Clonar el repo
git clone [https://github.com/tu-usuario/comapues.git](https://github.com/tu-usuario/comapues.git)

# Entrar a la carpeta
cd comapues

# Instalar dependencias
npm install

# Levantar el Backend
npx json-server --watch db.json --port 3001

# Ejecutar la aplicacion
npm run dev
