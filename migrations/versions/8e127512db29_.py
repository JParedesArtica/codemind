"""empty message

Revision ID: 8e127512db29
Revises: 
Create Date: 2023-10-10 04:05:18.487274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e127512db29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=40), nullable=True),
    sa.Column('question', sa.String(length=250), nullable=True),
    sa.Column('info_blog', sa.String(length=250), nullable=True),
    sa.Column('info_youtube', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=40), nullable=False),
    sa.Column('lastName', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('role', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token_blocked_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=1000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('module', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=40), nullable=True),
    sa.Column('answers', sa.String(length=250), nullable=True),
    sa.Column('exercise_id', sa.Integer(), nullable=True),
    sa.Column('isCorrect', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=40), nullable=False),
    sa.Column('lastName', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=400), nullable=False),
    sa.Column('img', sa.String(length=400), nullable=False),
    sa.Column('role', sa.String(length=150), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('answersuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('module', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=40), nullable=True),
    sa.Column('exercise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answersuser')
    op.drop_table('user')
    op.drop_table('answers')
    op.drop_table('token_blocked_list')
    op.drop_table('teacher')
    op.drop_table('exercise')
    # ### end Alembic commands ###