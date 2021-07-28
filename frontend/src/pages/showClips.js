import React, { useState, useEffect } from "react";
import { Route, Link, useHistory } from "react-router-dom";
import './showClips.css';
import axios from "axios";
import logoImg from './images/logo.png';
import Loading from './components/loading';
import ClipBox from './clipBox';

const EMOTIONS = ['Angry', 'Disgusting', 'Fearful', 'Happy', 'Sad', 'Surprising', 'Neutral']

// page 2
const ShowClips = (props) => {
    const videoIndex = props.location.state.videoIndex;
    const history = useHistory();
    const [load, setLoad] = useState(true);
    const [loading, setLoading] = useState(false);
    const [showBtn, setShowBtn] = useState(true);
    const leftBar = EMOTIONS.map((emotion, index) => (<li key={index} id="emotions">#{emotion}</li>))
    const [clips, setClips] = useState();

    // clip 5개 thumbnail, emotionlist 받기
    useEffect(() => {
        axios.get("/api/getClips/",{ 
            params: { 
                video_index: videoIndex, 
            }
        })
        .then(response => {
            if (response.data == {}){
                alert("Failed to show clips");
            }
            else {
                setClips(response.data);
            }
        })
        .catch(error => {
            console.log(error)
        })
    }, [])

    let clipNum = new Set();
    const checkboxHandler = (event, id) => {
        if (event.target.checked) {
            clipNum.add(id);
        }
        else {
            clipNum.delete(id);
        }
    }

    function getCheckedEmo() {
        return new Promise(function(resolve, reject){
            let checkedEmo = [];
            for (const value of clipNum){
                checkedEmo.push(clips[value].emotionlist[0])
            }
            resolve(checkedEmo)
        });
    }

    // function getResultImg() {
    //     return new Promise(function(resolve, reject){
    //         let resultImg = clips[clipNum[0]].thumbnail;
    //         resolve(resultImg)
    //     });
    // }
    
    async function selectHandler() {
        let checkedEmo = await getCheckedEmo();
        // let resultImg = await getResultImg();
        history.push({
            pathname: '/result',
            // state: { videoIndex : videoIndex, checkedEmo : checkedEmo, thumbnail : resultImg},
            state: { videoIndex : videoIndex, checkedEmo : checkedEmo }
        });
    }

    // 선택된 clip들 보냄 (0 base)
    // concatenate 완료 response 받으면
    // page3으로 (with videoIndex + 선택된 clip들의 emotion[0])
    const selectBtnHandler = () => {
        setShowBtn(false);
        setLoading(true);
        let str = [...clipNum].join("");

        axios.get("/api/getNums/", { 
            params: { 
                video_index: videoIndex,
                clipNum : str, 
            }
        })
        .then(response => {
            selectHandler();
        })
        .catch(error => {
            console.log(error);
        })
    }

    return (
        <>
        <div id="mainbox">
            <hr id="line1"></hr>
            <hr id="line2"></hr>
            <img id="logo" src={ logoImg }/>
            <div class="leftbar">
                <ul>
                    { leftBar }
                </ul>
            </div>
            <div class="videos">
                { clips && clips.map((clip) => ( 
                    <ClipBox thumbnail={clip.thumbnail} emotionlist={clip.emotionlist} /> 
                ))}
            </div>

            {/* <span class="checkbox" style = {load ? { visibility : "hidden" } : { visibility: "visible" }}> */}
            <span class="checkbox">
                <input type="checkbox" id="c1" onChange = { (e) => checkboxHandler(e, 0) }></input><br/>
                <input type="checkbox" id="c2" onChange = { (e) => checkboxHandler(e, 1) }></input><br/>
                <input type="checkbox" id="c3" onChange = { (e) => checkboxHandler(e, 2) }></input><br/>
                <input type="checkbox" id="c4" onChange = { (e) => checkboxHandler(e, 3) }></input><br/>
                <input type="checkbox" id="c5" onChange = { (e) => checkboxHandler(e, 4) }></input>
            </span>

            <button 
                class="btn" id="selectButton" onClick = { selectBtnHandler } 
                // style = {showBtn ? { visibility : "visible" } : { visibility: "hidden" }}
                >
                    select
            </button>

            <div id="load">{load? <Loading/> : ""}</div>
            <div id="loading2">{loading? <Loading/> : ""}</div>
        </div>
        </>
    )
}

export default ShowClips;