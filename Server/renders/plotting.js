// Scene setup
const scene = new THREE.Scene();
// var hostname = process.env.HOSTNAME || 'localhost';
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create points
const points = [];
for (let i = 0; i < 100; i++) {
    points.push(new THREE.Vector3(
        Math.random() * 20 - 10, // x
        Math.random() * 20 - 10, // y
        Math.random() * 20 - 10  // z
    ));
    
}

// points.push(new THREE.Vector3(
//     3, 4, 5
// ));
const geometry = new THREE.BufferGeometry().setFromPoints(points);
const material = new THREE.PointsMaterial({ color: 0xFF0000, size: 0.1 });
const pointsMesh = new THREE.Points(geometry, material);

scene.add(pointsMesh);

// Camera position
camera.position.z = 5;

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

animate();