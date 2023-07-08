"""create product table

Revision ID: df5d14120a6e
Revises: 
Create Date: 2023-07-08 10:11:09.312901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df5d14120a6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('type', sa.Integer),
        sa.Column('date', sa.DateTime),
        sa.Column('product', sa.String(100)),
        sa.Column('value', sa.Float),
        sa.Column('seller', sa.String(100)),
    )
    pass


def downgrade() -> None:
    op.drop_table('product')
    pass
