# Launches

## Tornyol: micro-drones that kill mosquitoes

TLDR We’re eradicating mosquitoes (700k people killed each year) with micro-drones.

Hey YC!

[Clovis Piedallu](https://www.linkedin.com/in/clovispiedallu/) and [Alex Toussaint](https://www.linkedin.com/in/alex-toussaint-51a439189/) are building [Tornyol](https://tornyol.com/), **a micro-drone that kills mosquitoes**. We use smartphone microphones, car park assist sensors and some clever DSP and control to transform 40-gram toy drones into mosquito killers. Because these drones are so cheap and fast, we could lower the cost of mosquito control by 100x to enable the eradication of malaria.

Our upcoming product is a micro-drone + base station that patrols your garden 24/7 and eliminates any mosquito in the zone. After a few days of action, you’ll notice that you can enjoy mosquito-free evenings and dinners. Enjoy a mosquito-free life for just $50/month (if you save your spot **right now for just $100**)!

https://www.youtube.com/watch?v=dDa9pFzeJvE

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95287&key=user_uploads/1250342/2697e87e-51cb-405e-bf8b-e4446880f4cc)

# How it started

Alex has been passionate about ultrasonic sonars for a while, building [one of the first air-gapped ultrasonic phased array sonars.](https://www.alextoussaint.com/2021-04-28_How-I-built-an-ultrasonic-3d-scanner.html) Alex then worked at MBDA Systems, supplier of UK-FR missiles where he did outstanding work in navigation and control. That’s when long-time friend [@Clovis Piedallu](https://bookface.ycombinator.com/user/2515354) and him had the (at first) stupid idea of building mosquito-killing drones. After proving from napkin math that this could lead to mosquito eradication, we got a $28k grant from [Scott Alexander, Vitalik Buterin](https://manifund.org/projects/build-anti-mosqu) and [some big twitter buzz.](https://x.com/alextoussss/status/1778460625196261863) Since, we’ve made enormous strides in the field including the first detection and tracking of a mosquito with an ultrasonic phased array, plus some fancy algorithms which are detailed more [here](https://hackaday.com/2025/03/25/supercon-2024-killing-mosquitoes-with-freaking-drones-and-sonar). We’ve made a lot of progress since in the control department, but can’t share much more without nuking an ongoing patent. The TLDR of that is **we believe we can eradicate mosquitoes from a square kilometer of land with just 10 40-grams drones, slashing the cost of mosquito control by 100x**

# The tech, with a few more details

We send an ultrasonic pulse using a regular ultrasonic transmitter (the one you can find in the HC-SR04 arduino modules, or on cark park assist sensors) then listen for the echoes using an array of smartphone microphones. This phased array of smartphone microphone allows us to get a directional recording of all echoes in the scene. To classify the echoes, we plot a spectrogram of the echoes as a function of time. Whenever a mosquito beats its wings, the movement produces irregular doppler effect. By measuring that alternating doppler effect, we get a 2D image that’s unique to each mosquito. We then detect the species and sex of the target we have in front of us. Here’s what these signatures look like.

**Wasp (phase, STFT, FFT)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95287&key=user_uploads/1250342/e34717d5-91b3-435f-b7b3-33eacfa00d77)

**Mosquito (phase, STFT, FFT)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95287&key=user_uploads/1250342/21bf0588-a122-48c8-9a62-60426d8e7b94)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95287&key=user_uploads/1250342/8bb71855-e1f9-4ea0-922f-06da6690c1c5)

Our phased array sonar (Xilinx XC7A100T and 380 PDM Microphones). We’ve miniaturized it since.

Then, by using some very clever control algorithms, we ram our autonomous tinywhoop into the mosquitoes and away from the walls.

# Our current development status

Most systems are working in isolation, and we’re doing a push to have them all working together. Our miniaturized DSP+Controls processor is currently in the PCB factory, and all algorithms have been tested either on separate benches or in simulation. We’re currently killing mosquitoes in simulation, and are working hard to kill them in the real world.

# Asks

Mosquitoes are a terrible problem worldwide **700k people killed each year, 700M catching a mosquito-borne disease and 4 billion people at risk of Dengue**.

We’re looking for early adopters for who mosquitoes are a big nuisance to proof-test our first drones when they work before we deploy them to areas where failure’s not an option. If that sounds like you, please pre-order and enjoy all the perks (limited edition color, 30% discount) that come from our small $100 refundable reservation.

# CTA

[tornyol.com](http://tornyol.com): $100 refundable deposit to get exclusive, early and discounted acess to our solution.

[founders@tornyol.com](mailto:founders@tornyol.com):\_for any contacts to big businesses, government entities and NGOs who could be clients.

Looking forward to your questions!

[Clovis Piedallu](https://www.linkedin.com/in/clovispiedallu/) and [Alex Toussaint](https://www.linkedin.com/in/alex-toussaint-51a439189/) for a mosquito-free world.
