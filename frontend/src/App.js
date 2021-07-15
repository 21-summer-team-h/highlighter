import axios from 'axios';

var fileDownload = require('js-file-download');
function App() {
    const handlePDFDownload = () => {
        axios.get('http://localhost:8000/download', { 
            responseType: 'blob',
        }).then(res => {
            fileDownload(res.data, 'filename.mp4');
            console.log(res);
        }).catch(err => {
            console.log(err);
        })
}
return (
    <div>
       <button
          onClick={() => handlePDFDownload()}>Download File!
       </button>
    </div>
    )
}

export default App;
