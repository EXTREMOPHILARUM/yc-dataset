# Launches

## renderlet: Making graphics programming easy

**Building interactive graphics is really hard**. Developers need expert-level knowledge of GPU programming just to build code that is not portable to new environments such as Web or Mobile or reusable across applications.

Renderlet is a WebAssembly framework for **writing graphics code that runs anywhere**. Describe your graphics pipeline using a **higher-level abstractions** and use renderlet to generate low-level, cross-platform rendering code.

With renderlet, developers can easily embed GPU-accelerated 2D and 3D graphics into cross-platform applications.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79415&key=user_uploads/1759368/4ce27e3c-1c68-456d-a0bd-eedd272c1712)

## How it works

With renderlet, **we compile graphics to portable WebAssembly modules** and provide a runtime that abstracts away the underlying GPU architecture to the code.

Developers can take advantage of modern technologies like **WebGPU** without having to learn the intricacies of yet another standard. 2D and 3D graphics are fully decoupled from the application and device and can ship decoupled from the applications code in a format that **runs anywhere**.

Renderlet is:

* A **compiler** that takes a high-level specification of your graphics pipeline - including custom assets, functions, and libraries - and builds self-contained WebAssembly rendering modules
* A  **renderer**, _wander_, that embeds into any application on any platform that and safely runs rendering modules with the GPU
* A **visual editor** that makes it easy to build entire graphics and visualization pipelines out of reusable rendering modules

**Anybody should be able to build interactive applications** without having to be a graphics programming expert.  

## About Us

[Sean Isom](https://linkedin.com/in/isom) previously built developer platforms at Adobe as a Lead Engineer and Sr. Engineering Manager. He helped bring products to the cloud and web using tools like WebAssembly and is currently involved in standardization efforts for WebAssembly GPU support.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79415&key=user_uploads/1759368/36bcf46c-edd6-4b90-9124-45c3c81ec64b)

## What’s next?

Our cross-platform rendering engine, **wander**, is open source: <https://github.com/renderlet/wander/> 

We’re kicking off with a **live demo** today of renderlet at Wasm I/O!  <https://2024.wasmio.tech/sessions/paint-by-numbers-high-performance-drawing-in-wasm/> 

Want more info on cross-platform graphics? **Get in touch**! - [sean@renderlet.com](mailto:sean@renderlet.com)
