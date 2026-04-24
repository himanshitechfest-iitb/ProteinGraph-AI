<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Bioinformatics | The Ultimate Engine</title>
    <style>
        body { margin: 0; overflow: hidden; background-color: #050505; font-family: 'Segoe UI', sans-serif; color: white; }
        #canvas-container { width: 100vw; height: 100vh; position: absolute; top: 0; left: 0; z-index: 1; }
        
        /* Glassmorphism UI Panels */
        .panel { position: absolute; z-index: 10; background: rgba(10, 14, 20, 0.85); backdrop-filter: blur(12px); padding: 25px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.6); }
        
        /* Left Panel - Controls */
        #left-panel { top: 20px; left: 20px; width: 340px; max-height: 90vh; overflow-y: auto;}
        
        /* Right Panel - Education */
        #right-panel { top: 20px; right: 20px; width: 380px; max-height: 90vh; overflow-y: auto; display: none; border-top: 4px solid #58a6ff; }
        
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: rgba(0,0,0,0.2); }
        ::-webkit-scrollbar-thumb { background: #30363d; border-radius: 4px; }
        
        h2 { margin-top: 0; font-size: 1.5rem; color: #fff; font-weight: 300; letter-spacing: 1px;}
        h2 span { font-weight: bold; color: #58a6ff; }
        h3 { font-size: 1.1rem; color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 5px; margin-top: 20px;}
        
        select { width: 100%; padding: 12px; background: rgba(0,0,0,0.8); color: white; border: 1px solid #30363d; border-radius: 6px; font-size: 1rem; margin: 15px 0;}
        optgroup { background: #0d1117; color: #58a6ff; font-weight: bold; }
        option { color: white; background: #0d1117; font-weight: normal; }

        .btn-group { display: flex; flex-direction: column; gap: 10px; margin-top: 15px;}
        button { padding: 12px; background: #238636; color: white; border: none; border-radius: 6px; font-size: 1rem; cursor: pointer; font-weight: bold; transition: all 0.2s;}
        button:hover { filter: brightness(1.2); }
        button:disabled { background: #1a4a22; cursor: not-allowed; opacity: 0.5; }
        
        #btn-mutate { background: #da3633; display: none;}
        #btn-render { background: #1f6feb; display: none;}

        .legend-box { background: rgba(0,0,0,0.4); padding: 15px; border-radius: 8px; border: 1px solid #30363d; margin-top: 20px; font-size: 0.9rem;}
        .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; margin-right: 10px; vertical-align: middle;}
        
        /* Right Panel Data Styling */
        .bio-item { margin-bottom: 15px; }
        .bio-label { font-size: 0.8rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 3px;}
        .bio-value { font-size: 1.05rem; font-weight: 400; line-height: 1.4; color: #e6edf3;}
        .org-value { font-style: italic; color: #d2a8ff; font-weight: 500;}
        .highlight-box { background: rgba(88, 166, 255, 0.1); padding: 12px; border-radius: 6px; border-left: 3px solid #58a6ff; margin-bottom: 15px; font-size: 0.95rem; line-height: 1.5; color: #c9d1d9;}
        .special-box { background: rgba(63, 185, 80, 0.1); padding: 12px; border-radius: 6px; border-left: 3px solid #3fb950; font-size: 0.95rem; line-height: 1.5; color: #c9d1d9;}

        #readout { margin-top: 20px; display: none; }
        .step { color: #8b949e; font-family: monospace; font-size: 0.9rem; margin-bottom: 8px; transition: color 0.3s;}
        .step.active { color: #58a6ff; font-weight: bold; }

        .alert-box { padding: 15px; border-radius: 8px; border-left: 4px solid; background: rgba(0,0,0,0.5); font-size: 0.95rem; line-height: 1.5; margin-top: 20px; display: none;}
        .status-normal { border-color: #3fb950; color: #e6edf3;}
        .status-danger { border-color: #da3633; color: #ff7b72; animation: pulse 2s infinite;}
        
        @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(218, 54, 51, 0.4); } 70% { box-shadow: 0 0 0 10px rgba(218, 54, 51, 0); } 100% { box-shadow: 0 0 0 0 rgba(218, 54, 51, 0); } }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    
    <div id="left-panel" class="panel">
        <h2>AI <span>Bioinformatics</span></h2>
        <p style="font-size: 0.9rem; color: #c9d1d9;">Select from 20 models to run 3D Graph Inference and Mutation physics.</p>
        
        <select id="pdb-select">
            <option value="" disabled selected>-- Select an Enzyme --</option>
            <optgroup label="EC 1: Oxidoreductases">
                <option value="1a3d">1A3D (Cytochrome c)</option>
                <option value="1bg5">1BG5 (Alcohol Dehydrogenase)</option>
                <option value="1dgb">1DGB (Catalase)</option>
                <option value="1n2c">1N2C (Nitrogenase)</option>
            </optgroup>
            <optgroup label="EC 2: Transferases">
                <option value="1hex">1HEX (Hexokinase)</option>
                <option value="3pgk">3PGK (Phosphoglycerate kinase)</option>
                <option value="1taq">1TAQ (Taq DNA Polymerase)</option>
                <option value="1d09">1D09 (Aspartate Transcarbamoylase)</option>
            </optgroup>
            <optgroup label="EC 3: Hydrolases">
                <option value="3lzt">3LZT (Lysozyme)</option>
                <option value="1cvd">1CVD (Beta-galactosidase)</option>
                <option value="2ach">2ACH (Acetylcholinesterase)</option>
                <option value="1pso">1PSO (Pepsin)</option>
            </optgroup>
            <optgroup label="EC 4: Lyases">
                <option value="4enl">4ENL (Enolase)</option>
                <option value="1rcx">1RCX (Rubisco)</option>
                <option value="1ca2">1CA2 (Carbonic Anhydrase)</option>
            </optgroup>
            <optgroup label="EC 5: Isomerases">
                <option value="1tim">1TIM (Triosephosphate Isomerase)</option>
                <option value="9xia">9XIA (Xylose Isomerase)</option>
                <option value="1mek">1MEK (Protein Disulfide Isomerase)</option>
            </optgroup>
            <optgroup label="EC 6: Ligases">
                <option value="1a0i">1A0I (DNA Ligase)</option>
                <option value="2gls">2GLS (Glutamine Synthetase)</option>
            </optgroup>
        </select>

        <div class="btn-group">
            <button id="btn-load" disabled>Run Inference Pipeline</button>
            <button id="btn-render">Toggle Space-Filling Volume</button>
            <button id="btn-mutate">Simulate Point Mutation</button>
        </div>

        <div class="legend-box">
            <div style="color:#58a6ff; font-weight:bold; margin-bottom:10px;">How the AI sees Biology:</div>
            
            <div style="margin-bottom: 8px;">
                <span class="dot" style="background:#58a6ff;"></span> 
                <strong>Nodes:</strong> C-Alpha Amino Acids.
            </div>
            
            <div style="margin-bottom: 15px;">
                <span class="dot" style="background:#8b949e; height:2px; border-radius:0;"></span> 
                <strong>Edges:</strong> Spatial Proximity (< 8Å).
            </div>
            
            <div style="border-top: 1px solid #30363d; padding-top: 12px;">
                <strong>Topographical Coloring:</strong>
                <p style="font-size: 0.8rem; color: #8b949e; margin: 5px 0;">
                    Nodes are colored using HSL math based on their exact sequence index. This traces the continuous 1D chain as it folds into 3D space.
                </p>
                
                <div style="height: 10px; width: 100%; background: linear-gradient(to right, hsl(0, 85%, 55%), hsl(60, 85%, 55%), hsl(120, 85%, 55%), hsl(180, 85%, 55%), hsl(240, 85%, 55%), hsl(288, 85%, 55%)); border-radius: 4px; margin: 10px 0 4px 0; border: 1px solid #000;"></div>
                
                <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-weight: bold; color: #c9d1d9;">
                    <span>N-Terminus (Start)</span>
                    <span>C-Terminus (End)</span>
                </div>
            </div>
        </div>

        <div id="readout">
            <div id="step-1" class="step">> Extracting Backbone...</div>
            <div id="step-2" class="step">> Building Proximity Graph...</div>
            <div id="step-3" class="step">> Pooling Global Topology...</div>
        </div>

        <div id="alert-display" class="alert-box status-normal"></div>
    </div>

    <div id="right-panel" class="panel">
        <h2 id="bio-name">Enzyme Data</h2>
        
        <div style="width: 100%; height: 200px; background: rgba(0,0,0,0.6); border-radius: 8px; border: 1px solid #30363d; margin-top: 15px; margin-bottom: 15px; overflow: hidden; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 0 10px rgba(0,0,0,0.8);">
            <img id="bio-image" src="" alt="Protein Structure" style="max-width: 100%; max-height: 100%; object-fit: contain; display: none;">
        </div>

        <div class="bio-item">
            <div class="bio-label">Source Organism</div>
            <div id="bio-org" class="bio-value org-value"></div>
        </div>
        <div class="bio-item">
            <div class="bio-label">Catalytic Function</div>
            <div id="bio-func" class="bio-value"></div>
        </div>

        <h3>Data Pipeline Processing</h3>
        <div style="display: flex; gap: 15px; margin-bottom: 15px; background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; border: 1px solid #30363d;">
            <div style="flex: 1; text-align: center;">
                <div style="font-size: 0.7rem; color: #8b949e; text-transform: uppercase;">Raw Atoms</div>
                <div id="stat-total" style="font-size: 1.2rem; color: #d2a8ff; font-weight: bold;">0</div>
            </div>
            <div style="flex: 1; text-align: center; border-left: 1px solid #30363d; border-right: 1px solid #30363d;">
                <div style="font-size: 0.7rem; color: #8b949e; text-transform: uppercase;">Graph Nodes</div>
                <div id="stat-nodes" style="font-size: 1.2rem; color: #58a6ff; font-weight: bold;">0</div>
            </div>
            <div style="flex: 1; text-align: center;">
                <div style="font-size: 0.7rem; color: #8b949e; text-transform: uppercase;">8Å Edges</div>
                <div id="stat-edges" style="font-size: 1.2rem; color: #8b949e; font-weight: bold;">0</div>
            </div>
        </div>
        
        <h3>Structural Insights</h3>
        <div class="bio-label">What to Notice in the 3D Graph:</div>
        <div id="bio-notice" class="highlight-box"></div>
        
        <h3>Biological Significance</h3>
        <div class="bio-label">Why this Enzyme is Famous:</div>
        <div id="bio-special" class="special-box"></div>
    </div>

    <div id="canvas-container"></div>

    <script>
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x050505, 0.008);
        
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0xffffff, 0.8);
        pointLight.position.set(50, 50, 50);
        scene.add(pointLight);

        const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 120;
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.getElementById('canvas-container').appendChild(renderer.domElement);
        
        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.autoRotate = true;
        controls.autoRotateSpeed = 1.5;
        controls.enableDamping = true;

        let currentGraph = new THREE.Group();
        scene.add(currentGraph);

        let nodeMeshes = [];
        let edgesMesh = null;
        let isSpaceFilling = false;
        let isMutated = false;

        const btnLoad = document.getElementById('btn-load');
        const btnRender = document.getElementById('btn-render');
        const btnMutate = document.getElementById('btn-mutate');
        const select = document.getElementById('pdb-select');
        const rightPanel = document.getElementById('right-panel');
        const readout = document.getElementById('readout');
        const alertDisplay = document.getElementById('alert-display');

        select.addEventListener('change', () => { btnLoad.disabled = false; });

        function activateStep(index) {
            [1,2,3].forEach(i => {
                const step = document.getElementById('step-'+i);
                if(i === index) step.classList.add('active');
                else step.classList.remove('active');
            });
        }

        btnLoad.addEventListener('click', async () => {
            const pdbId = select.value;
            btnLoad.disabled = true;
            btnRender.style.display = 'none';
            btnMutate.style.display = 'none';
            rightPanel.style.display = 'none';
            readout.style.display = 'block';
            alertDisplay.style.display = 'none';
            activateStep(1);
            isSpaceFilling = false;
            isMutated = false;
            btnMutate.innerText = "Simulate Point Mutation";
            btnMutate.disabled = false;
            
            scene.remove(currentGraph);
            currentGraph = new THREE.Group();
            scene.add(currentGraph);
            nodeMeshes = [];

            try {
                const res = await fetch(`/api/predict?pdb_id=${pdbId}`);
                const data = await res.json();
                if(data.error) { alert(data.error); btnLoad.disabled = false; return; }

                // Right Panel Data Population
                document.getElementById('bio-name').innerText = data.name.toUpperCase() + ` (${data.prediction})`;
                document.getElementById('bio-org').innerText = data.organism;
                document.getElementById('bio-func').innerText = data.function;
                document.getElementById('bio-notice').innerText = data.notice;
                document.getElementById('bio-special').innerText = data.special;
                
                // RCSB Dynamic Image Fetching
                const imgElement = document.getElementById('bio-image');
                imgElement.src = `https://cdn.rcsb.org/images/structures/${pdbId}_assembly-1.jpeg`;
                imgElement.style.display = 'block';

                // Data Pipeline Stats
                if(data.stats) {
                    document.getElementById('stat-total').innerText = data.stats.total_raw_atoms.toLocaleString();
                    document.getElementById('stat-nodes').innerText = data.stats.ai_nodes_extracted.toLocaleString();
                    document.getElementById('stat-edges').innerText = data.stats.spatial_edges_formed.toLocaleString();
                }

                rightPanel.style.display = 'block';

                activateStep(2);
                
                // Draw 3D Graph
                const nodeGeo = new THREE.SphereGeometry(1.2, 16, 16);
                const nodeMat = new THREE.MeshPhongMaterial({ color: 0x30363d, shininess: 50 });
                
                data.nodes.forEach(pos => {
                    const sphere = new THREE.Mesh(nodeGeo, nodeMat.clone());
                    sphere.position.set(pos[0], pos[1], pos[2]);
                    currentGraph.add(sphere);
                    nodeMeshes.push(sphere);
                });

                const edgeGeo = new THREE.BufferGeometry();
                const edgePositions = [];
                for(let i=0; i<data.edges[0].length; i++) {
                    const u = data.edges[0][i];
                    const v = data.edges[1][i];
                    edgePositions.push(...data.nodes[u]);
                    edgePositions.push(...data.nodes[v]);
                }
                edgeGeo.setAttribute('position', new THREE.Float32BufferAttribute(edgePositions, 3));
                const edgeMat = new THREE.LineBasicMaterial({ color: 0x8b949e, transparent: true, opacity: 0.15 });
                edgesMesh = new THREE.LineSegments(edgeGeo, edgeMat);
                currentGraph.add(edgesMesh);

                // AI Processing Animation
                setTimeout(() => {
                    activateStep(3);
                    nodeMeshes.forEach(n => {
                        if(Math.random() > 0.6) n.material.color.setHex(0xd2a8ff); 
                    });
                }, 1500);

                setTimeout(() => {
                    activateStep(0);
                    
                    // NEW CODE: Beautiful N-to-C Terminus Rainbow Gradient!
                    // We calculate the color based on the node's position in the chain
                    const totalNodes = nodeMeshes.length;
                    
                    nodeMeshes.forEach((n, index) => {
                        // Calculate a hue from 0.0 to 1.0 based on index
                        // We multiply by 0.8 so it stops at purple/magenta instead of looping back to red
                        const hue = (index / totalNodes) * 0.8; 
                        
                        // .setHSL(hue, saturation, lightness)
                        n.material.color.setHSL(hue, 0.85, 0.55); 
                    }); 
                    
                    btnRender.style.display = 'block';
                    btnMutate.style.display = 'block';
                    
                    alertDisplay.className = "alert-box status-normal";
                    alertDisplay.style.display = 'block';
                    alertDisplay.innerHTML = `<strong>Status:</strong> Fold Stable<br><span style="font-weight:bold; color:#3fb950; font-size:1.2rem;">Prediction: ${data.prediction}</span><br>AI Confidence: ${data.confidence}%`;
                    
                    btnLoad.disabled = false;
                }, 3500);

            } catch (err) {
                alert("Server error. Is python arjun.py running?");
                btnLoad.disabled = false;
            }
        });

        // Toggle Space-Filling Volume
        btnRender.addEventListener('click', () => {
            isSpaceFilling = !isSpaceFilling;
            const targetScale = isSpaceFilling ? 3.5 : 1.0;
            nodeMeshes.forEach(mesh => {
                new TWEEN.Tween(mesh.scale).to({x: targetScale, y: targetScale, z: targetScale}, 800).easing(TWEEN.Easing.Quadratic.Out).start();
            });
            if(edgesMesh) {
                new TWEEN.Tween(edgesMesh.material).to({opacity: isSpaceFilling ? 0 : 0.15}, 800).start();
            }
        });

        // Simulate Point Mutation
        btnMutate.addEventListener('click', () => {
            if(isMutated) return;
            isMutated = true;
            btnMutate.disabled = true;
            btnMutate.innerText = "Steric Clash Simulated!";

            const targetIdx = Math.floor(nodeMeshes.length / 2) + Math.floor(Math.random() * 10);
            const targetNode = nodeMeshes[targetIdx];

            targetNode.material.color.setHex(0xda3633); // Red Alert
            new TWEEN.Tween(targetNode.scale).to({x: 8, y: 8, z: 8}, 1000).easing(TWEEN.Easing.Elastic.Out).start();

            nodeMeshes.forEach((mesh, idx) => {
                if(idx !== targetIdx && mesh.position.distanceTo(targetNode.position) < 15) {
                    mesh.material.color.setHex(0xff7b72); 
                    new TWEEN.Tween(mesh.position)
                        .to({
                            x: mesh.position.x + (Math.random()-0.5)*5,
                            y: mesh.position.y + (Math.random()-0.5)*5,
                            z: mesh.position.z + (Math.random()-0.5)*5
                        }, 500).start();
                }
            });

            alertDisplay.className = "alert-box status-danger";
            alertDisplay.innerHTML = `<strong>CRITICAL ERROR:</strong> Steric Clash at Residue ${targetIdx}.<br>Active site folding bonds destroyed.<br><span style="font-weight:bold; color:#ff7b72; font-size:1.1rem;">AI Confidence: 12.4% (Loss of Function)</span>`;
        });

        function animate(time) {
            requestAnimationFrame(animate);
            TWEEN.update(time);
            controls.update();
            renderer.render(scene, camera);
        }
        
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
        animate();
    </script>
</body>
</html>
