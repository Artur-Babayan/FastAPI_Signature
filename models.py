from sqlalchemy import Column, Integer, String, Float
from database import Base


class Signaturs(Base):
    __tablename__ = "signaturs"

    id = Column(Integer, primary_key=True, index=True)
    NAME = Column(String)
    MHCI = Column(Float)
    MHCII = Column(Float)
    Coactivation_molecules = Column(Float)
    Effector_cells = Column(Float)
    T_cell_traffic = Column(Float)
    NK_cells = Column(Float)
    T_cells = Column(Float)
    B_cells = Column(Float)
    M1_signatures = Column(Float)
    Th1_signature = Column(Float)
    Antitumor_cytokines = Column(Float)
    Checkpoint_inhibition = Column(Float)
    Treg = Column(Float)
    T_reg_traffic = Column(Float)
    Neutrophil_signature = Column(Float)
    Granulocyte_traffic = Column(Float)
    MDSC = Column(Float)
    MDSC_traffic = Column(Float)
    Macrophages = Column(Float)
    Macrophage_DC_traffic = Column(Float)
    Th2_signature = Column(Float)
    Protumor_cytokines = Column(Float)
    CAF = Column(Float)
    Matrix = Column(Float)
    Matrix_remodeling = Column(Float)
    Angiogenesis = Column(Float)
    Endothelium = Column(Float)
    Proliferation_rate = Column(Float)
    EMT_signature = Column(Float)
