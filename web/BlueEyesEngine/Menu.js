/*****************************************************/
/*                  BlueEyes Engine                  */
/*                  Menu                             */
/*                                                   */
/* Version 1.0.10                                    */
/* Date 2022/12/21                                   */
/* Coded by Cenlun Chung Po Lun                      */
/*****************************************************/

const Menu = document.querySelector(".Menu");

// Pop-up menu
function openMenu(){
    document.querySelector(".Menu").style.display = "flex";
};

// Press "Escape" to open menu
function whenEscPressed(e) {

    if (e.key == 'Escape') {

        if(document.querySelector(".Menu").style.display == "flex"){
            document.querySelector(".Menu").style.display = "none";
            document.querySelector(".MenuContent").style.display = "block";
            document.querySelector(".AboutContent").style.display = "none";
        }
        else{
            openMenu();    
        }
        
    }
}

document.addEventListener('keyup', whenEscPressed, false);

//Untitiled

function showAbout(){
    document.querySelector(".MenuContent").style.display="none";
    document.querySelector(".AboutContent").style.display="block";
}

function backToMenu(){
    document.querySelector(".MenuContent").style.display="block";
    document.querySelector(".AboutContent").style.display="none";
}

function backToCurrent(){
    document.querySelector(".Menu").style.display = "none";
}