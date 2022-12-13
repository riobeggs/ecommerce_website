"""Added OrderItems model

Revision ID: 35e20f88ec9a
Revises: d3cd8c7dbb9b
Create Date: 2022-12-14 00:09:59.632301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "35e20f88ec9a"
down_revision = "d3cd8c7dbb9b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "order_items",
        sa.Column("order_items_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("order_id", sa.Integer(), nullable=True),
        sa.Column("item_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["item_id"],
            ["item.item_id"],
        ),
        sa.ForeignKeyConstraint(
            ["order_id"],
            ["order.order_id"],
        ),
        sa.PrimaryKeyConstraint("order_items_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order_items")
    # ### end Alembic commands ###
