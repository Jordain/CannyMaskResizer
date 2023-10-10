const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const imageInput = document.getElementById('imageInput');

function handleImage() {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
                // Scale and position the image
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 600, 700, 300, 50); // Change the dimensions as needed
            };
        };
        reader.readAsDataURL(file);
    }
}
