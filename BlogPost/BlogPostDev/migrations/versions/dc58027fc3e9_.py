"""empty message

Revision ID: dc58027fc3e9
Revises: 
Create Date: 2020-05-24 22:04:47.873497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc58027fc3e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_image', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Blogs',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('profile_image', sa.String(length=20), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('timeofPost', sa.DateTime(), nullable=False),
    sa.Column('post_text', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Blogs')
    op.drop_table('users')
    # ### end Alembic commands ###
