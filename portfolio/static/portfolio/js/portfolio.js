
/**
 * Global Event listeners
 */
 $(".btnOne").click(function () {
    $('.btnOne').addClass('active');
    $('.btnTwo').removeClass('active');
    photoGridOne();
});

$(".btnTwo").click(function () {
    $('.btnTwo').addClass('active')
    $('.btnOne').removeClass('active')
    $('.btnThree').removeClass('active')
    $('.btnFour').removeClass('active')
    photoGridTwo();
});

$(".btnThree").click(function () {
    $('.btnThree').addClass('active')
    $('.btnOne').removeClass('active')
    $('.btnTwo').removeClass('active')
    $('.btnFour').removeClass('active')
    photoGridThree();
});

$(".btnFour").click(function () {
    $('.btnFour').addClass('active')
    $('.btnOne').removeClass('active')
    $('.btnTwo').removeClass('active')
    $('.btnThree').removeClass('active')
    photoGridFour();
});


/**
 * function to enable the view of one photo per column
 * on small screens, else two
 */
 const photoGridOne = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-12', 'col-sm-6'])
    $('#photoGridRow>div.photoGrid').removeClass('col-6')
};

/**
 * function to enable the view of three photos per column
 * on screens larger than small, else two.
 */
const photoGridThree = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-4', 'col-6'])
    $('#photoGridRow>div.photoGrid').removeClass(['col-sm-3', 'col-sm-6'])
};

/**
 * function to enable the view of two photos per column
 * on screens larger than small, else two
 */

const photoGridTwo = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-6', 'col-6'])
    $('#photoGridRow>div.photoGrid').removeClass(['col-sm-3', 'col-sm-4', 'col-12'])
};

/**
 * function to enable the view of Four photos per column
 * on screens larger than small, else two
 */
const photoGridFour = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-3', 'col-6'])
    $('#photoGridRow>div.photoGrid').removeClass(['col-sm-4', 'col-sm-6', 'col-12'])
};
