/**
 * Global Event listeners
 */
 $(".btnOne").click(function () {
    $('.btnOne').addClass('active')
    photoGridOne();
});

$(".btnTwo").click(function () {
    $('.btnTwo').addClass('active')
    photoGridTwo();
});

$(".btnThree").click(function () {
    $('.btnThree').addClass('active')
    photoGridThree();
});

$(".btnFour").click(function () {
    $('.btnFour').addClass('active')
    photoGridFour();
});


/**
 * function to enable the view of one photo per column
 */
 const photoGridOne = () => {
    $('#photoGridRow>div.photoGrid').addClass('col-12')
    $('#photoGridRow>div.photoGrid').removeClass('col-6')
    $('.btnTwo').removeClass('active')
};

/**
 * function to enable the view of three photos per column
 */
const photoGridThree = () => {
    $('#photoGridRow>div.photoGrid').addClass('col-4')
    $('#photoGridRow>div.photoGrid').removeClass('col-3')
    $('#photoGridRow>div.photoGrid').removeClass('col-6')
    $('.btnTwo').removeClass('active')
    $('.btnFour').removeClass('active')
};

/**
 * function to enable the view of two photos per column
 */

const photoGridTwo = () => {
    $('#photoGridRow>div.photoGrid').removeClass('col-3')
    $('#photoGridRow>div.photoGrid').removeClass('col-4')
    $('#photoGridRow>div.photoGrid').removeClass('col-12')
    $('#photoGridRow>div.photoGrid').addClass('col-6')
    $('.btnOne').removeClass('active')
    $('.btnThree').removeClass('active')
    $('.btnFour').removeClass('active')
};

/**
 * function to enable the view of Four photos per column
 */
const photoGridFour = () => {
    $('#photoGridRow>div.photoGrid').removeClass('col-4')
    $('#photoGridRow>div.photoGrid').removeClass('col-6')
    $('#photoGridRow>div.photoGrid').addClass('col-3')
    $('.btnOne').removeClass('active')
    $('.btnTwo').removeClass('active')
    $('.btnThree').removeClass('active')
};
