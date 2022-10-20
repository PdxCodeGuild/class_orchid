// Get the image and insert it inside the modal - use its "alt" text as a caption
function bigger(id){
    
    const modal = document.getElementById(`myModal${id}`);
    const modalIMG = document.getElementById(`modal${id}`)
    const img = document.getElementById(id)
    const span = document.getElementById(`close${id}`);
    const captionText = document.getElementById(`caption${id}`);

    modal.style.display = "flex";
    modalIMG.src = img.src;
    captionText.innerHTML = img.alt;

    span.onclick = function() {
        modal.style.display = "none";
    }
}
