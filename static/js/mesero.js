document.querySelectorAll(".plato-button").forEach(button => {
    button.addEventListener("click", async () => {
        const id_plato = button.querySelector(".id_plato").textContent.trim();
        const nombre_plato = button.querySelector(".nombre_plato").textContent.trim();
        const productosDePlato = await obtenerProductosAsociados(id_plato);

        // Renderizar el plato y sus productos en el panel de pedido
        agregarPlatoAPanel(nombre_plato, id_plato, productosDePlato);
    });
});

const obtenerProductosAsociados = async (id_plato) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/platoProductos/${id_plato}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error(`Status: ${response.status}`);

        const data = await response.json();
        console.log("🔍 Respuesta de la API:", JSON.stringify(data, null, 2));

        // Verificar si data es un array
        if (!Array.isArray(data)) {
            throw new Error("❌ La API no devolvió un array.");
        }

        // Extraer solo los valores de fk_producto
        const productosIds = data.map(item => {
            console.log("📌 Item procesado:", item);
            return item.fk_producto;
        }).filter(id => id !== undefined);

        console.log("✅ Lista de productos extraída:", productosIds);

        if (productosIds.length === 0) {
            throw new Error("❌ No se encontraron productos válidos en la respuesta.");
        }

        // Llamar a obtenerProducto() para cada ID
        const productosDePlato = await Promise.all(productosIds.map(id => obtenerProducto(id)));

        return productosDePlato;
    } catch (error) {
        console.error("🚨 Error al obtener productos asociados:", error);
        return [];
    }
};

const obtenerProducto = async (producto_id) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/productosPlato/${producto_id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error(`Error al cargar los productos: ${response.status}`);

        return await response.json();
    } catch (error) {
        console.error("Error al obtener producto ${producto_id}:, error");
        return null;
    }
};

const agregarPlatoAPanel = (nombre_plato, id_plato, productosDePlato) => {
    const panelDePedido = document.querySelector(".panelDePedido");

    // Crear el contenedor del plato
    const pedidoItem = document.createElement("div");
    pedidoItem.classList.add("pedido-item", "flex", "justify-between", "flex-col");

    pedidoItem.innerHTML = `
        <span><b>Plato:</b><br>${nombre_plato}</span>
        <input type='hidden' name='plato' value='${id_plato}'>
        <div class="productosdelplato flex flex-col rounded border-2 border-yellow-400 p-1">
            <h2><b>Productos del plato:</b></h2>
        </div>
    `;

    panelDePedido.appendChild(pedidoItem);

    // Seleccionar la nueva sección de productos creada dentro de este plato
    const selectProductos = pedidoItem.querySelector(".productosdelplato");

    productosDePlato.forEach(producto => {
        if (producto) {
            selectProductos.innerHTML += `
                <div class="flex flex-row w-5/6 mb-2 ml-1 justify-between">
                    <label class="w-3/4">${producto.nombre_producto}</label>
                    <input type="checkbox" name="productoPlato" value="${id_plato}-${producto.id}" checked>

                    <button type="button" class="logopencil" data-id="${id_plato}-${producto.id}">
                        <div hidden class="id_producto">${producto.id}</div>
                        <img src="/static/images/lapicito.png" alt="Editar">
                    </button>
                </div>
            `;
        }
    });
};

let currentLapizButton; // Variable global para mantener la referencia al botón del lápiz

// Gestión del modal
document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modal");
    const closeModalButton = document.getElementById("close-modal");
    const modalContent = document.getElementById("modal-content");

    modal.style.display = "none"; // Oculta el modal al cargar la página

    document.body.addEventListener("click", async (event) => {
        if (event.target.closest(".logopencil")) {
            currentLapizButton = event.target.closest(".logopencil");

            const productoId = currentLapizButton.dataset.id;
            await cargarProductosEnModal(productoId);
            modal.style.display = "flex"; // Mostrar el modal
        }
    });

    closeModalButton.addEventListener("click", () => {
        modal.style.display = "none"; // Ocultar el modal
    });
});

// Cargar los productos en el modal
const cargarProductosEnModal = async () => {
    const modalContent = document.getElementById("modal-content");
    const modalTitle = document.querySelector("h2");

    try {
        const response = await fetch("http://127.0.0.1:8000/api/productosPlato/");
        if (!response.ok) throw new Error(`Error al cargar los productos: ${response.status}`);

        const productos = await response.json();

        modalTitle.textContent = "Productos Disponibles";
        modalContent.innerHTML = ""; // Limpia el contenido previo

        modalContent.innerHTML = productos.map(producto => `
            <button class="producto-card bg-blue-100 p-4 rounded-lg shadow-md hover:shadow-lg transition" data-id="${producto.id}">
                <div class="hidden">${producto.id}</div>
                <div class="font-bold text-lg">${producto.nombre_producto}</div>
                <div class="text-sm text-gray-700">${producto.descripcion_producto}</div>
                <div class="font-semibold text-md mt-2">$${producto.precio_producto}</div>
            </button>
        `).join('');

        // Manejar el evento de clic en los productos dentro del modal
        document.querySelectorAll(".producto-card").forEach(card => {
            card.addEventListener("click", () => {
                const selectedId = card.querySelector(".hidden").textContent;
                const selectedNombre = card.querySelector(".font-bold").textContent;

                // Ahora usamos la variable global currentLapizButton
                const productoId = currentLapizButton.dataset.id;

                // Actualiza el producto seleccionado en el panel
                actualizarProductoSeleccionado(productoId, selectedId, selectedNombre);
                modal.style.display = "none"; // Cerrar el modal
            });
        });
    } catch (error) {
        console.error("Error al cargar los productos:", error);
        alert("Ocurrió un error al cargar los productos. Inténtalo nuevamente.");
    }a
};

// Función para actualizar el producto seleccionado en el panel
const actualizarProductoSeleccionado = (productoId, newProductId, newProductName) => {
    // Extraer id_plato y id_producto del productoId
    const [id_plato, existingProductId] = productoId.split('-');

    // Seleccionar todos los divs que contienen los productos en el pedido
    const pedidoItems = document.querySelectorAll('.pedido-item');

    pedidoItems.forEach(div => {
        // Encontrar los checkboxes relacionados
        const checkboxes = div.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            if (checkbox.value === productoId) { // Verificar que coincide con el producto que se está editando
                // Marcar el checkbox
                checkbox.checked = true;

                // Actualizar el valor oculto del input asociado al producto
                checkbox.value = `${id_plato}-${newProductId}`;

                // Actualizar el nombre del producto mostrado
                const label = checkbox.closest('.flex').querySelector('label');
                if (label) {
                    label.textContent = newProductName; // Actualizar el nombre en la etiqueta
                }
            }
        });
    });
};

// BUSQUEDA DE ITEMS
document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const items = document.querySelectorAll(".buscar");

    searchInput.addEventListener("input", function () {
        const searchTerm = searchInput.value.toLowerCase().trim();

        items.forEach(item => {
            const text = item.textContent.toLowerCase();
            const parentCard = item.closest(".item");

            if (text.includes(searchTerm)) {
                parentCard.style.display = "block"; // Mostrar si coincide
            } else {
                parentCard.style.display = "none"; // Ocultar si no coincide
            }
        });
    });
});



//LOGICA BUSQUEDA DE ELEMENTOS
// document.addEventListener('DOMContentLoaded', () => {
//     const searchInput = document.getElementById('search-input');
//     const searchButton = document.getElementById('search-button');
//     const platosContainer = document.getElementById('platos-container');
//     const productosContainer = document.getElementById('productos-container');

//     // Función para realizar la búsqueda
//     const realizarBusqueda = async () => {
//         const query = searchInput.value.trim();

//         try {
//             const response = await fetch(`http://127.0.0.1:8000/pedidos/buscar/?q=${encodeURIComponent(query)}`);
//             if (!response.ok) throw new Error(`Error en la solicitud: ${response.status}`);

//             const data = await response.json();
//             actualizarResultados(data);
//         } catch (error) {
//             console.error('Error al realizar la búsqueda:', error);
//         }
//     };

//     // Función para actualizar los resultados en la interfaz
//     const actualizarResultados = (data) => {
//         // Limpiar los contenedores actuales
//         platosContainer.innerHTML = '';
//         productosContainer.innerHTML = '';

//         // Renderizar los platos encontrados
//         data.platos.forEach(plato => {
//             const platoDiv = document.createElement('div');
//             platoDiv.classList.add('item', 'flex', 'flex-col', 'bg-white', 'rounded-lg', 'shadow-md', 'p-2', 'transition', 'transform', 'hover:scale-105');
//             platoDiv.innerHTML = `
//                 <button class="button-item plato-button w-full">
//                     <div class="flex flex-col items-center">
//                         <img src="#" alt="${plato.nombre_plato}" class="rounded-t-lg mb-2 h-24 w-full object-cover">
//                         <div class="id_plato hidden">${plato.id}</div>
//                         <div class="nombre_plato font-semibold text-sm">${plato.nombre_plato}</div>
//                         <div class="descripcion_plato text-xs text-gray-600 text-center">${plato.descripcion_plato}</div>
//                         <div class="precio mt-1 text-lg text-green-500">$${plato.precio}</div>
//                     </div>
//                 </button>
//             `;
//             platosContainer.appendChild(platoDiv);
//         });

//         // Renderizar los productos encontrados
//         data.productos.forEach(producto => {
//             const productoDiv = document.createElement('div');
//             productoDiv.classList.add('item', 'flex', 'flex-col', 'bg-white', 'rounded-lg', 'shadow-md', 'p-2', 'transition', 'transform', 'hover:scale-105');
//             productoDiv.innerHTML = `
//                 <button class="button-item producto-button w-full">
//                     <div class="flex flex-col items-center">
//                         <img src="#" alt="${producto.nombre_producto}" class="rounded-t-lg mb-2 h-24 w-full object-cover">
//                         <div class="id_producto hidden">${producto.id}</div>
//                         <div class="nombre_producto font-semibold text-sm">${producto.nombre_producto}</div>
//                         <div class="descripcion_producto text-xs text-gray-600 text-center">${producto.descripcion_producto}</div>
//                         <div class="precio mt-1 text-lg text-green-500">$${producto.precio_producto}</div>
//                     </div>
//                 </button>
//             `;
//             productosContainer.appendChild(productoDiv);
//         });
//     };

//     // Asignar eventos al input y al botón de búsqueda
//     searchInput.addEventListener('input', realizarBusqueda);
//     searchButton.addEventListener('click', realizarBusqueda);
// });




//MI CODIGO
// document.querySelectorAll(".plato-button").forEach(button => {
//     button.addEventListener("click", async () => {

//         const id_plato = button.querySelector(".id_plato").textContent.trim();
//         const nombre_plato = button.querySelector(".nombre_plato").textContent.trim();

//         console.log(id_plato, nombre_plato);

//         try {
//             const response = await fetch(`http://127.0.0.1:8000/api/platoProductos/${id_plato}`, {
//                 "method": "GET",
//                 "headers": {
//                     "Content-Type": "application/json",
//                 }
//             });
//             if (!response.ok) {
//                 console.error(`Status: ${response.status}, Text : ${response.statusText}`);
//                 alert("Error al realizar la petición");
//                 return; // Salir si la petición falla
//             }

//             const data = await response.json();
//             console.log("Respuesta del servidor:", data);

//             const productosDePlato = []

//             //BUCLE QUE ITERA SOBRE CADA ID DE LOS PRODUCTOS ASOCIADOS AL PLATO ELEGIDO/ACTUAL
//             for (const producto_id of data.productos) {
//                 try {
//                     const responseProducto = await fetch(`http://127.0.0.1:8000/api/productosPlato/${producto_id}`, {
//                         "method": "GET",
//                         "headers": {
//                             "Content-Type": "application/json",
//                         },
//                     });

//                     if (!responseProducto.ok) {
//                         console.error(`Status: ${responseProducto.status}, Text : ${responseProducto.statusText}`);
//                         alert("Error al realizar la petición del producto");
//                         continue;
//                     }

//                     const dataProducto = await responseProducto.json();
//                     productosDePlato.push(dataProducto)


//                 } catch (error) {
//                     console.error("Error al obtener los productos del plato:", error);
//                 }
//             };
//             //FIN BUCLE

//             // Mostrar el plato o producto seleccionado en el pedido
//             const panelDePedido = document.querySelector(".panelDePedido");
//             panelDePedido.innerHTML += `
//                 <div class='pedido-item flex justify-between flex flex-col'>
//                     <span><b>Plato:</b><br>${nombre_plato}</span>
//                     <input type='hidden' name='plato' value='${id_plato}'>

//                     <div class = "productosdelplato flex flex-col rounded rounded-lg border border-2 border-yellow-400 p-1">
//                         <h2><b>Productos del plato:</b></h2>
//                     </div>
//                 </div>`;

//             const selects = panelDePedido.querySelectorAll(".productosdelplato");
//             const selectProductos = selects[selects.length - 1]; // Selecciona el último <select>

//             for(const producto of productosDePlato){
//                 selectProductos.innerHTML += `
//                 <div class="flex flex-row w-5/6 mb-2 ml-1 justify-between">
//                     <label class ="w-3/4" name = "productoPlato">${producto.nombre_producto}</label>
//                     <input  class = "_${id_plato}_${producto.id}"type ="checkbox" name = "productoPlato" value =${id_plato}-${producto.id} checked>

//                     <button type = "button" class = "logopencil">
//                         <div hidden class = "id_producto hidden"> ${id_plato}_${producto.id} </div>
//                         <img src="/static/images/lapicito.png" alt="Editar">
//                     </button>
//                 </div>
//                 `
//             }

//         } catch (error) {
//             console.error("Error al realizar la solicitud:", error);
//             alert("Ocurrió un error de red o en el servidor.");
//         }
//     });
// });

// document.querySelectorAll(".producto-button").forEach(button => {
//     button.addEventListener("click", async()=>{
//         const id_producto = button.querySelector(".id_producto").textContent.trim();
//         const nombre_producto = button.querySelector(".nombre_producto").textContent.trim();
//         const panelPedido = document.querySelector(".panelDePedido")
        
        
//         panelPedido.innerHTML += `<p>${nombre_producto}</p><input type="hidden" name = "producto" value = "${id_producto}">`
//     })

// })

// document.addEventListener("DOMContentLoaded", () => {
//     // Elementos del modal
//     const modal = document.getElementById("modal");
//     const modalContent = document.getElementById("modal-content");
//     const closeModalButton = document.getElementById("close-modal");
//     const modalTitle = document.querySelector("h2");

//     // Evento para detectar clics en el icono de lápiz
//     document.body.addEventListener("click", async (event) => {
//         event.preventDefault();
//         const lapizButton = event.target.closest(".logopencil"); // Verifica si se hizo clic en el icono del lápiz
//         const id_producto_elegido = lapizButton.querySelector(".id_producto").textContent ;
//         const guardar_id_producto = document.querySelector(".id_producto_elegido")
//         console.log(id_producto_elegido)
//         guardar_id_producto.textContent = `${id_producto_elegido}`;


//         if (lapizButton) {
//             try {
//                 // Cargar los productos de la API
//                 const response = await fetch("http://127.0.0.1:8000/api/productosPlato/");
//                 if (!response.ok) {
//                     throw new Error(`Error al cargar los productos: ${response.status}`);
//                 }

//                 const productos = await response.json();

//                 // Generar el contenido del modal como botones de cartas
//                 modalTitle.textContent = "Productos Disponibles";
//                 modalContent.innerHTML = productos.map(producto => `
//                     <button class="producto-card bg-blue-100 p-4 rounded-lg shadow-md hover:shadow-lg transition">
//                         <div class="hidden">${producto.id}</div>
//                         <div class="font-bold text-lg">${producto.nombre_producto}</div>
//                         <div class="text-sm text-gray-700">${producto.descripcion_producto}</div>
//                         <div class="font-semibold text-md mt-2">$${producto.precio_producto}</div>
//                     </button>
//                 `).join('');

//                 // Mostrar el modal
//                 modal.style.display = "flex"; // Muestra el modal
//             } catch (error) {
//                 console.error("Error al cargar los productos:", error);
//                 alert("Ocurrió un error al cargar los productos. Inténtalo nuevamente.");
//             }
//         }

        
//     });

//     // Cerrar el modal
//     closeModalButton.addEventListener("click", () => {
//         modal.style.display = "none"; // Ocultar el modal
//     });
// });

// document.querySelectorAll(".producto-card").forEach(card => {
//     card.addEventListener("click", ()=>{
//         id_elegido = document.querySelector(".id_producto_elegido").textContent
//         console.log("El id que se trajo fue: ", id_elegido)
//     })
// })