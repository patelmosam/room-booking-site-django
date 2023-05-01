document.addEventListener('DOMContentLoaded', function() {
  // Your code here


    const date_field_1 = document.getElementById('date-input-1')
    const date_field_2 = document.getElementById('date-input-2')

    const parentHtmlTag = document.getElementById('parent-to-booking-message')
    const btn_check_cart = document.getElementById('btnCheck')

    const form = document.getElementById('form-inline')



     form.addEventListener('submit', ev => {

        // Validate inputs
        const isValid = validateInputs();
        // If inputs are invalid, prevent form submission
        if (!isValid) {
            ev.preventDefault();
        }

    });

     const setMessage = (element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.booking-message');

        errorDisplay.innerText = message;
        inputControl.classList.add('error');
        inputControl.classList.remove('success')
    }

    const setError =(element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = message;
        inputControl.classList.add('error');
        inputControl.classList.remove('success')
    }

    const validateInputs = () => {
        const date_field_1Value = date_field_1.value;
        const date_field_2Value = date_field_2.value;

        const dateObject_1 = new Date (date_field_1Value)
        const dateObject_2 = new Date (date_field_2Value)

        const datetime_difference = (dateObject_2 - dateObject_1)/1000;

        if(datetime_difference < 0){
            setError(date_field_2, 'Oops!, your end of stay date cannot be less than your start date');
        }else if(datetime_difference < 86400){
            setError(date_field_2, 'Oops!, you must book for at least one day');
        }
        else {
            return true;
        }
    }

    const display_book_infor = () => {
        const date_field_1Value = date_field_1.value;
        const date_field_2Value = date_field_2.value;

        const price = parentHtmlTag.className;


        const dateObject_1 = new Date (date_field_1Value)
        const dateObject_2 = new Date (date_field_2Value)

        const datetime_difference = (dateObject_2 - dateObject_1)/1000;

        const number_of_days = datetime_difference/86400;
        const total_price= price*number_of_days;

        const days_r_h= datetime_difference % 86400;
        const hours= days_r_h/3600;
        /* divide the above to get hours */

        const hour_r_m= days_r_h % 3600;
        const mins= hour_r_m/60;
        /*divide the above to get the mins */


        setMessage(
            parentHtmlTag, `You have ${Math.floor(number_of_days)} day(s), ${Math.floor(hours)}hour(s), ${Math.floor(mins)}min(s) of your stay and your total cost is USD $ ${total_price.toFixed(2)}`);
    }

        btn_check_cart.addEventListener('click', ev => {
        ev.preventDefault();
        display_book_infor()

    });

});