"""create account table

Revision ID: b68256ac7ada
Revises: 
Create Date: 2018-05-31 20:59:32.934666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b68256ac7ada'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('slug', sa.String(length=30), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('published', sa.DateTime, nullable=True),
    sa.Column('timestamp', sa.DateTime, nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('posts')
