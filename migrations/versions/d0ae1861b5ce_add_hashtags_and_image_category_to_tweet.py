"""Add hashtags and image_category to Tweet

Revision ID: d0ae1861b5ce
Revises: 31b27e2b23df
Create Date: 2025-05-22 16:41:31.911413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0ae1861b5ce'
down_revision = '31b27e2b23df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashtags', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('image_category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tweet', schema=None) as batch_op:
        batch_op.drop_column('image_category')
        batch_op.drop_column('hashtags')

    # ### end Alembic commands ###
