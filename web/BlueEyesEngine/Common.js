/*****************************************************/
/*                  BlueEyes Engine                  */
/*                  Common                           */
/*                                                   */
/* Version 1.0.10                                    */
/* Date 2022/12/21                                   */
/* Coded by Cenlun Chung Po Lun                      */
/*****************************************************/

// Close App
function closeApp(){
    window.close();
};

// Disable Context Menu
document.oncontextmenu = ()=>{
    return false;
};

// Disable Image Drag
const img = document.querySelector('img')
img.ondragstart = () => {
    return false;
};