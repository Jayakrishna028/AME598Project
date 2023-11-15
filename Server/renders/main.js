import * as THREE from 'three';

// console.log('human')
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 90, window.innerWidth / window.innerHeight, 0.1, 10000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry(1, 1, 1)
const material = new THREE.MeshBasicMaterial( { color: 0x00fff0 } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 3;

function animate() {
	requestAnimationFrame( animate );

	cube.rotation.z += 0.01;
	cube.rotation.y += 0.01;
    cube.rotation.x += 0.01;

	renderer.render( scene, camera );
}

animate();