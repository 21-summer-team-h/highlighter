import React, {useState} from "react";
import "./showClips.css"
const EMOTIONS = ['Angry', 'Disgusting', 'Fearful', 'Happy', 'Sad', 'Surprising', 'Neutral']

const ClipBox = (props) => {

    let thumbnail = props.thumbnail;
    thumbnail = JSON.stringify(thumbnail);
    thumbnail = thumbnail.replace(/\"/g,'');
    let emotionlist = props.emotionlist;

    function Emotion(props) {
        return <span>#{EMOTIONS[props.value]} </span>
    }

    function EmotionList(props) {
        const emotions = props.emotions;
        const list = emotions.map((e) =>
            <Emotion key={e.toString()} value={e}/>
        );
        return (
            <>
            {list}
            </>
        )
    }

    return (
        <div class="videoBox">
            <img src={"data:image/png;base64,"+ thumbnail } class="videoThumbnail"></img>
            <span class="videoEmotions">
                <EmotionList emotions={ emotionlist }/>
            </span>
        </div>
    )
}

export default ClipBox;