"use_client"

import Image from 'next/image'

export default function Home() {

    let stream;
    const startWebcam = () => {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then((mediaStream) => {
            stream = mediaStream;
            video.srcObject = stream;
            video.play();
        })
        .catch((err) => {
            console.error('Error accessing the webcam: ' + err);
        });
    }
    const stopWebcam = () => {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
            // Get modal elements
            const modal = document.getElementById("myModal");
            const openModalButton = document.getElementById("openModalButton");
            const closeModalSpan = document.getElementsByClassName("close")[0];

            // Open the modal
            openModalButton.onclick = function() {
                modal.style.display = "block";
                startWebcam();
            }

            // Close the modal
            closeModalSpan.onclick = function() {
                modal.style.display = "none";
                stopWebcam();
            }

            // Close the modal if the user clicks outside of the modal content
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                    stopWebcam();
                }
            }

            // Access the video element
            const video = document.getElementById('video');
            let stream;

            // Get access to the webcam
            function startWebcam() {

            }

            // Stop the webcam
            function stopWebcam() {
                if (stream) {
                    stream.getTracks().forEach(track => track.stop());
                }
            }

            // Capture the image when the button is clicked
            const captureButton = document.getElementById('captureButton');
            captureButton.addEventListener('click', () => {
                // Access the canvas element
                const canvas = document.getElementById('canvas');
                const context = canvas.getContext('2d');

                // Draw the current frame from the video onto the canvas
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                // Get the data URL of the captured image
                const dataUrl = canvas.toDataURL('image/png');

                // Display the captured image
                const capturedImage = document.getElementById('capturedImage');
                capturedImage.src = dataUrl;
                capturedImage.style.display = 'block';

                // Close the modal
                modal.style.display = "none";
                stopWebcam();
            });
        });

  return (
    <main
      className="flex flex-col items-center justify-between p-24"
      style={{
        minHeight: '350vh', // 3 times the screen height
        backgroundImage: 'url(img/finalbg.png)',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
    >
      <h2
        className="changing-hue"
        style={{
          color: 'yellow',
          fontSize: '90px',
          zIndex: 1000,
          lineHeight: '0.9',
          textAlign: 'center',
          position: 'absolute',
          left: '600px',
          bottom: '-570px',
        }}
      >
        the <br></br>wortal
      </h2>

      <img
        className="expando"
        src="/img/smwhere.png"
        style={{
          height: '100vh',
          width: '140vh',
          position: 'absolute',
          left: 'auto',
          right: 'auto',
          bottom: '-250px',
        }}
      ></img>

      <img
        className="rotating-changing-hue"
        src="/img/wortal.png"
        style={{
          height: '100vh',
          width: '140vh',
          position: 'absolute',
          left: 'auto',
          right: 'auto',
          bottom: '-900px',
        }}
      />

      <img
        className="rotating-changing-hue"
        src="/img/wortal.png"
        style={{
          height: '100vh',
          width: '140vh',
          position: 'absolute',
          left: 'auto',
          right: 'auto',
          bottom: '-900px',
        }}
      />

      <img
        className="changing-hue"
        src="/img/heyyou.png"
        style={{
          height: 'auto',
          width: '30vh',
          position: 'absolute',
          left: 'auto',
          right: 'auto',
          top: '50px',
        }}
      />

      <img
        className="rotating-changing-hue"
        src="/img/wiz.png"
        style={{
          height: 'auto',
          width: '25vh',
          position: 'absolute',
          left: '70px',
          bottom: '-300px',
        }}
      />

      <img
        className="rotating-changing-hue"
        src="/img/wiz.png"
        style={{
          height: 'auto',
          width: '25vh',
          position: 'absolute',
          left: '90px',
          bottom: '-800px',
        }}
      />

      <img
        className="rotating-changing-hue"
        src="/img/wiz.png"
        style={{
          height: 'auto',
          width: '25vh',
          position: 'absolute',
          right: '90px',
          bottom: '-500px',
        }}
      />

      {/* <h1 className="text-4xl font-bold">Welcome to Manakin</h1> */}
      <div className="flex flex-col items-center">
        <button className="absolute rotating left-0 top-12 button text-black text-4xl px-[40px]">
          yes you
        </button>
        <button className="absolute rotating right-0 top-1/4 button text-black text-4xl px-[40px]">
          yes you
        </button>
        <button className="absolute rotating left-12 top-1/4 button text-black text-4xl px-[40px]">
          yes you
        </button>
        <button className="absolute rotating right-12 top-12 button text-black text-4xl px-[40px]">
          yes you
        </button>
      </div>
      <div className="flex flex-col items-center">
        <button
          className="button text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2"
          style={{
            height: '340px',
            width: '840px',
            position: 'absolute',
            left: '100px',
            bottom: '-1580px',
            backgroundImage: 'url(img/button1.png)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        ></button>
        <button
          className="button"
          style={{
            height: '330px',
            width: '870px',
            position: 'absolute',
            left: '450px',
            bottom: '-1880px',
            backgroundImage: 'url(img/button2.png)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
          onClick={startWebcam}
        ></button>
      </div>
      <div className="flex flex-col items-center"></div>
    </main>
  )
}
