"""merge heads

Revision ID: ce27405c4513
Revises: 85da5e95ced7, 9fa966bb0f4e
Create Date: 2026-11-16 17:45:17.202810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce27405c4513'
down_revision = ('85da5e95ced7', '9fa966bb0f4e')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
