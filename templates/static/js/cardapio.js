// admin_area.html
document.addEventListener("DOMContentLoaded", () => {
    console.log("js_loaded")
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

    const qrCodeModalBtn = document.querySelector("#qrCodeModalBtn")
    const qrCodeCloseModalBtn = document.querySelector("#qrCodeCloseModalBtn")

    const qrCodeModal = document.querySelector("#qrCodeModal")

    qrCodeModalBtn.addEventListener("click", (event) => {
        qrCodeModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })

    qrCodeCloseModalBtn.addEventListener("click", (event) => {
        qrCodeModal.classList.toggle("hide")
        boxShadow.classList.toggle("hide")
        body.classList.toggle("overflow")
    })
})
