/**
 * Global Event listeners
 */
$(".btnOne").click(function () {
    $('button.active').removeClass('active')
    $(this).addClass('active')
    photoGridOne();
});

$(".btnTwo").click(function () {
    $('button.active').removeClass('active')
    $(this).addClass('active')
    photoGridTwo();
});

$(".btnThree").click(function () {
    $('button.active').removeClass('active')
    $(this).addClass('active')
    photoGridThree();
});

$(".btnFour").click(function () {
    $('button.active').removeClass('active')
    $(this).addClass('active')
    photoGridFour();
});

/**
 * function to enable the view of one photo per column
 * on small screens, else two
 */
const photoGridOne = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-12', 'col-sm-6']).removeClass('col-6')
};

/**
 * function to enable the view of three photos per column
 * on screens larger than small, else two.
 */
const photoGridThree = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-4', 'col-6']).removeClass(['col-sm-3', 'col-sm-6', 'col-12'])
};

/**
 * function to enable the view of two photos per column
 * on screens larger than small, else two
 */

const photoGridTwo = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-6', 'col-6']).removeClass(['col-sm-3', 'col-sm-4', 'col-12'])
};

/**
 * function to enable the view of Four photos per column
 * on screens larger than small, else two
 */
const photoGridFour = () => {
    $('#photoGridRow>div.photoGrid').addClass(['col-sm-3', 'col-6']).removeClass(['col-sm-4', 'col-sm-6', 'col-12'])
};
