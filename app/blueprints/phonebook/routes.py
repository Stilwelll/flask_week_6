from . import phonebook as pb
from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from .forms import itemForm
from .models import Item


@pb.route('/')
def index():
    commerce = Item.query.all()
    title = 'Home'
    return render_template('index.html', title = title, pb = commerce)



@pb.route('/itementry', methods = ["GET", "POST"])
@login_required
def phonebookentry():
    title = 'phone book entry'
    form = itemForm()

    if form.validate_on_submit():
        item_name = form.item_name.data 
        new_pbook = Item(item_name=item_name, user_id = current_user.id)
        flash(f"{item_name} has been added to your PhoneBook.", "primary")
        return redirect(url_for('phonebook.itementry'))

    return render_template('itementry.html', title = title, form = form)

@pb.route('/myitems')
@login_required
def myphonebook():
    title = "My PhoneBook Entries"
    books = current_user.items.all()
    return render_template('myitems.html', title = title, books = books)

@pb.route('/edit-item/<contact_id>', methods=["GET", "POST"])
@login_required 
def edit_contact(contact_id):
    contact = Item.query.get_or_404(contact_id)
    #Check if the user trying to edit the post is the current user
    if contact.author != current_user:
        flash("You do not have edit access for this contact.", "danger")
        return redirect(url_for('phonebook.myphonebook'))
    title = f"Edit Contact: {{ contact.first_name }}"
    form = itemForm()
    if form.validate_on_submit():
        contact.update(**form.data)
        flash(f"{contact.first_name} has been updated.", "success")
        return redirect(url_for('phonebook.myitems'))
    return render_template('edit_item.html', title=title, contact=contact, form=form)

@pb.route('/delete_item/<contact_id>')
@login_required
def delete_contact(contact_id):
    contact = Item.query.get_or_404(contact_id)
    if contact.author != current_user:
        flash("You do not have delete access to this item.", 'secondary')
    else:
        contact.delete()
        flash(f"{contact} has been removed.", 'secondary')
    return redirect(url_for('phonebook.myitems'))