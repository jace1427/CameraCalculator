import React, {useState, useEffect} from 'react';
import axios from 'axios';
import './App.css';

const ApiMessenger = () => {

    const [hash, setHash] = useState(null);
    const [img, setImg] = useState<string>("");
    const [output, setOutput] = useState<string>("");


    const handleSubmit = (event:any) => {
        event.preventDefault();

        let formData = new FormData();
        formData.append("file", event.target[0].files[0]);

        axios({
            method: "POST",
            url: "http://0.0.0.0:3000/uploader",
            data: formData,
            headers: { "Content-Type": "multipart/form-data" },
        })
        .then((response) => {
            //handle success
            console.log(response);
            setHash(response.data);
        })
        .catch((response) => {
            //handle error
            console.log(response);
        });
    }

    const handleImageChange = (event:any) => {
        setImg(URL.createObjectURL(event.target.files[0]));
    }

    useEffect(() => {
      setTimeout(() => {  
        console.log(hash);
        axios.get('http://0.0.0.0:3000/' + hash)
        .then(response => {
            console.log(response);
            setOutput(response.data);
        }, error => {
            console.log(error);
        });
      }, 1000);
    }, [hash])

    return (
        <div className="ApiFrame">

            <div className="ImgFrame">
                {img && (<img alt="i <3 cs" width="100px" height="100px" src={img}/>)}
            </div>

            <form onSubmit={handleSubmit}>
                <input className="ImgInput" type="file" name="file" id="imgselect" onChange={handleImageChange} />
                <br/>
                <div className="ImgButton">
                    <label htmlFor="imgselect">Choose Image</label>
                </div>

                {img && (<button className="ImgButton" type="submit">Submit</button>)}


            </form> 

            {hash && (<p>File hash: {hash}</p>)} 
            {output && output !== "None"  && (<p>Output: {output}</p>)}

        </div>
        )
}


const App = () => {
  return (
  <div className="WebApp">
    <div className="Toolbar">
        Computer Vision Camera Calculator
    </div>
    <div className="App">
        <ApiMessenger/>
    </div>
  </div>
  );
}

export default App;
