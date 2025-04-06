document.addEventListener("DOMContentLoaded", function () {
    function addProduct(element) {
        const productId = element.getAttribute("data-id");

        // Verifica si ya está en la lista de seleccionados
        if (document.querySelector(`input[name="productos"][value="${productId}"]`)) {
            alert("Este producto ya está seleccionado.");
            return;
        }

        // Crea el tag en la lista de seleccionados
        const selectedContainer = document.getElementById("productos-seleccionados");
        const newTag = document.createElement("div");
        newTag.className = "selected-tag bg-blue-500 text-white rounded-full px-3 py-1 cursor-pointer";
        newTag.setAttribute("data-id", productId);
        newTag.innerHTML = `${element.textContent} <span class="ml-2 text-red-500" onclick="event.stopPropagation(); removeProduct(this.parentElement)">x</span>`;
        newTag.addEventListener("click", function () {
            removeProduct(newTag);
        });
        selectedContainer.appendChild(newTag);

        // Agrega un input hidden con el ID del producto seleccionado
        const hiddenInput = document.createElement("input");
        hiddenInput.type = "hidden";
        hiddenInput.name = "productos";
        hiddenInput.value = productId;
        selectedContainer.appendChild(hiddenInput);
    }

    function removeProduct(element) {
        const productId = element.getAttribute("data-id");

        // Elimina el tag seleccionado
        element.remove();

        // Elimina el input hidden correspondiente
        const hiddenInput = document.querySelector(`input[name="productos"][value="${productId}"]`);
        if (hiddenInput) {
            hiddenInput.remove();
        }
    }

    // Exponer funciones globalmente
    window.addProduct = addProduct;
    window.removeProduct = removeProduct;
});