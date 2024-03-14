"""Nodes coefficient

Revision ID: 77c86a261126
Revises: a0715c2615f0
Create Date: 2023-09-16 17:31:42.925189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77c86a261126'
down_revision = 'a0715c2615f0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nodes', sa.Column('usage_coefficient', sa.Float(), server_default=sa.text('1.0'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nodes', 'usage_coefficient')
    # ### end Alembic commands ###
