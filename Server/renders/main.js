var scene, camera, renderer;

function init() {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('threeContainer').appendChild(renderer.domElement);

    // Adjust camera position
    camera.position.z = 5;
    camera.position.y = -2;
    camera.lookAt(0, 0, 0);

    getDataFromServer();
    animate();
}

function getDataFromServer() {
    var url = "./getLatestThree";
    loadFile(url, function(data) {
        var points = JSON.parse(data);
        plotPoints(points);
    });
}

function plotPoints(points) {
    // Clear previous points
    while(scene.children.length > 0){ 
        scene.remove(scene.children[0]); 
    }

    points.forEach(dataPoint => {
        dataPoint.vectors.forEach((vector, index) => {
            // Create a geometry and set its vertices
            var geometry = new THREE.BufferGeometry();
            geometry.setAttribute('position', new THREE.BufferAttribute(new Float32Array([vector.x, -vector.y, -vector.z]), 3));

            // Create a material and define its color
            var material = new THREE.PointsMaterial({ color: getVectorColor(index), size: 0.2 });

            // Create a points object and add it to the scene
            var points = new THREE.Points(geometry, material);
            scene.add(points);
        });
    });
}

function getVectorColor(index) {
    // Define colors for each vector: front, right, and left
    const colors = [0xff0000, 0x00ff00, 0x0000ff];
    return colors[index] || 0xffffff; // Default to white if index is out of range
}

function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

// Adjust the scene when the window is resized
window.addEventListener('resize', onWindowResize, false);

function onWindowResize(){
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// Initialize the scene
init();
