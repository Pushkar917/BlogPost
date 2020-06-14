from flask import render_template, Blueprint, request
from companyBlog.models import BlogPosts

core = Blueprint('core', __name__)


@core.route('/')
def index():
    '''This is the home page'''
    '''It limits the no of post to be shown in a page'''
    ''' Limits the query size by calling paginate'''
    page = request.args.get('page', 1, type=int)
    blogposts = BlogPosts.query.order_by(BlogPosts.timeofPost.desc()).paginate(page=page,per_page=10)
    return render_template('index.html', posts=blogposts)


@core.route('/info')
def info():
    '''This is about passing the info of the page'''
    return render_template('info.html')
