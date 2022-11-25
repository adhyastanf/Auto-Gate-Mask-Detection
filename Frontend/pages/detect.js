import Webcam from "react-webcam";
import { useRef } from "react";
import { useEffect, useState } from "react";

function App() {
  const [result, setResult] = useState([]);

  let videoRef = useRef();
  let refButton = useRef();
  const imgURL = "https://teachablemachine.withgoogle.com/models/f3rdJMbyh/model.json";

    let detectInterval;
    useEffect(() => {
      const ml5 = require("ml5");
      const modelLoaded = () => {
        // videoRef.current.video;
        console.log('model ready')
        // detectInterval = setInterval(() => {
          refButton.current.onclick = () => detect()
        
          // }, 1000);
        };
        const classifier = ml5.imageClassifier(imgURL, modelLoaded);

    // Start image classification

    const detect = () => {
      classifier.classify(videoRef.current.video, (error, results) => {
        if (error) {
          console.error(error);
          return;
        }
        setResult(results[0]);
      });
    };

    return () => {
      if (detectInterval) {
        clearInterval(detectInterval);
      }
    };
  },[]);
  console.log(result)

  return (
    <div>
      <Webcam ref={videoRef} mirrored={true} style={{ display: "block" }} width={500} height={400} audio={false} video={"true"} />
      <button ref={refButton}>CLASSIFY</button>
      {result.label && <p>{result.label}</p>}
    </div>
  );
}

export default App;
