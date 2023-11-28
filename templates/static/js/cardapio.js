// detail_restaurant.html
document.addEventListener("DOMContentLoaded", () => {
    const newCategoryBtn = document.querySelector("#newCategoryBtn")
    const newCategoryModal = document.querySelector("#newCategoryModal")
    const closeCategoryModalBtn = document.querySelector("#closeCategoryModalBtn")

    const newProductBtn = document.querySelector("#newProductBtn")
    const newProductModal = document.querySelector("#newProductModal")
    const closeProductModalBtn = document.querySelector("#closeProductModalBtn")

    const boxShadow = document.querySelector("#box-shadow")
    const body = document.querySelector("body")

    newCategoryBtn.addEventListener("click", (event) => {
        newCategoryModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })
    closeCategoryModalBtn.addEventListener("click", (event) => {
        newCategoryModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })
    newProductBtn.addEventListener("click", (event) => {
        newProductModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })
    closeProductModalBtn.addEventListener("click", (event) => {
        newProductModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })
})