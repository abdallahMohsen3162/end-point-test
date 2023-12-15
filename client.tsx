// pages/index.tsx
import { useState, ChangeEvent, useEffect, useRef } from 'react';
import { NextPage } from 'next';

import axios from 'axios';


let str = "";

const Home = () => {
  const [url, seturl] = useState("")

  useEffect(() => {

    fetch('http://127.0.0.1/fet', {
    method: 'GET',
    // headers: {
    //   'Content-Type': 'image/png',
    // },
  }).then((res) => {
    return res.blob();
  }).then(blob => {
    const imageUrl = URL.createObjectURL(blob);
    const imageElement = document.getElementById('imageElement');
    console.log(imageUrl);
    seturl(imageUrl)
  })
  
  }, []);



  return (
    <div>
      <img src={url} alt="sad" />
    </div>
  );
};

export default Home;
