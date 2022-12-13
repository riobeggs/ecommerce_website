"""Added Address model

Revision ID: 4609aefcae6b
Revises: 
Create Date: 2022-12-14 00:39:05.187332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4609aefcae6b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("street", sa.String(length=64), nullable=True),
        sa.Column("suburb", sa.String(length=64), nullable=True),
        sa.Column("city", sa.String(length=64), nullable=True),
        sa.Column("postal_code", sa.String(length=64), nullable=True),
        sa.Column("country", sa.String(length=64), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("address")
    # ### end Alembic commands ###
