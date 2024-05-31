// Criar Constante

const images = [
    {src: "./Imagens/noticia-05.jpg", alt: "imagem 2"},
    {src: "./Imagens/sao-luis-maranhao-edit-27-600x399.jpg", alt: "imagem 3"},
    {src: "./Imagens/sao-luis.jpg", alt: "imagem 4"},
    {src: "./Imagens/Visit-Brazil-Sao-Luis-MA-Praia-e-Sol-7.jpg", alt: "imagem 5"}
];

const array_images = [
    {src: "./Imagens/noticia-05.jpg", alt: "imagem 2"},
    {src: "./Imagens/sao-luis-maranhao-edit-27-600x399.jpg", alt: "imagem 3"},
    {src: "./Imagens/sao-luis.jpg", alt: "imagem 4"},
    {src: "./Imagens/Visit-Brazil-Sao-Luis-MA-Praia-e-Sol-7.jpg", alt: "imagem 5"}
];

let index = 0;

function exibeGaleria() {
    const galeriaDiv = document.querySelector(".galeria");
    
    images.forEach(image => {
        const imgElement = document.createElement("img");
        imgElement.src = image.src;
        imgElement.alt = image.alt;
        galeriaDiv.appendChild(imgElement);
    });
}

function changeImage() {
    const slideshow = document.getElementById('slideshow');
    
    // Atualiza o conteúdo do slideshow com a próxima imagem
    slideshow.innerHTML = `<img src="${array_images[index].src}" alt="${array_images[index].alt}">`;
     
    index = (index + 1) % array_images.length; // Avança para a próxima imagem de forma cíclica
}
