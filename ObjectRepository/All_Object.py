class register_elem():
    register_btn = "register-button"
    firstname_txt = "FirstName"
    lastname_txt = "LastName"
    email_txt = "Email"
    genderMmale_btn = "gender-male"
    genderFemale_btn = "gender-female"
    password_txt = "Password"
    confirmPassword_txt = "ConfirmPassword"
    firstname_error_msg = "//span[@for='FirstName']"
    lastname_error_msg = "//span[@for='LastName']"
    email_eror_msg = "//span[@for='Email']"
    password_error_msg = "//span[@for='Password']"
    confirmPassword_error_msg = "//span[@for='ConfirmPassword']"
    existing_email_error_msg = "//li[text() = 'The specified email already exists' ]"

class login_elem():
    login_btn = "//input[@class='button-1 login-button']"
    remember_me_btn = "RememberMe"

class product_elem():
    computers_prd_menu = "//ul[@class='top-menu']//a[normalize-space()='Computers']"
    desktop_prd_sub_menu = "//ul[@class='top-menu']//a[normalize-space()='Desktops']"
    menu_title = "//h1[text() = 'Desktops' ]"
    add_to_cart_btn = "add-to-cart-button-72"
    shopping_cart_link = "//a[normalize-space()='shopping cart']"
    computer_item = "//h2[@class='product-title']//a[normalize-space()='Build your own cheap computer']"
    qty_txt = "addtocart_72_EnteredQuantity"
    qty_cart_elem = "cart-qty"
    notif_bar = "(//p[@class='content'])"
    cart = "ico-cart"
    checkout_btn = "checkout"
    termsofservice = "termsofservice"
    continue_btn = "//input[@class='button-1 new-address-next-step-button']"

    