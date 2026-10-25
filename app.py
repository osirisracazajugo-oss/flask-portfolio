from flask import Flask, render_template, request, redirect, url_for
from linkedlist import LinkedList
from stackalgorithm import Stack
from queue_deque import Queue, Deque          # NEW

st = Stack()

ll = LinkedList()

q = Queue()                                    # NEW
dq = Deque()                                   # NEW

def ll_items():
    items, cur = [], ll.head
    while cur:
        items.append(cur.data)
        cur = cur.next
    return items

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        result = round(3.14 * radius * radius, 2)
    return render_template('circle.html', result=result)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        result = 0.5 * base * height
    return render_template('triangle.html', result=result)

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)

@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '')
        if action == 'add_end' and value:
            ll.insert_at_end(value)
        elif action == 'add_start' and value:
            ll.insert_at_beginning(value)
        elif action == 'remove_first':
            ll.remove_beginning()
        elif action == 'remove_last':
            ll.remove_at_end()
        elif action == 'remove_value':
            ll.remove_at(value)
        elif action == 'search':
            message = "Found" if ll.search(value) else "Not found"
        elif action == 'insert_after':
            after = request.form.get('after', '')
            if value and after:
                ll.insert_after(after, value)
        if action != 'search':
            return redirect(url_for('linkedlist'))
    return render_template('linkedlist.html', items=ll_items(), message=message)

@app.route('/stack', methods=['GET', 'POST'])
def stack_page():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '')
        if action == 'push' and value:
            st.push(value)
            return redirect(url_for('stack_page'))
        elif action == 'pop':
            try:
                message = f"Popped: {st.pop()}"
            except IndexError:
                message = "Stack is empty"
        elif action == 'peek':
            try:
                message = f"Top: {st.peek()}"
            except IndexError:
                message = "Stack is empty"
    return render_template('stack.html', items=st.to_list()[::-1], size=st.size(), message=message)

# NEW: Queue and Deque page
@app.route('/queuedeque', methods=['GET', 'POST'])
def queuedeque():
    message = None
    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value', '')
        try:
            if action == 'enqueue' and value:
                q.enqueue(value)
            elif action == 'dequeue':
                message = f"Dequeued: {q.dequeue()}"
            elif action == 'peek':
                message = f"Front: {q.peek()}"
            elif action == 'add_front' and value:
                dq.add_front(value)
            elif action == 'add_rear' and value:
                dq.add_rear(value)
            elif action == 'remove_front':
                message = f"Removed front: {dq.remove_front()}"
            elif action == 'remove_rear':
                message = f"Removed rear: {dq.remove_rear()}"
            elif action == 'peek_front':
                message = f"Front: {dq.peek_front()}"
            elif action == 'peek_rear':
                message = f"Rear: {dq.peek_rear()}"
        except IndexError:
            message = "It's empty."
        if message is None:
            return redirect(url_for('queuedeque'))
    return render_template('queuedeque.html', q_items=q.to_list(),
                           d_items=dq.to_list(), message=message)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)