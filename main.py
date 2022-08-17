from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Signature(BaseModel):
    NAME: str = Field(min_length=1)
    MHCI: float
    MHCII: float
    Coactivation_molecules: float
    Effector_cells: float
    T_cell_traffic: float
    NK_cells: float
    T_cells: float
    B_cells: float
    M1_signatures: float
    Th1_signature: float
    Antitumor_cytokines: float
    Checkpoint_inhibition: float
    Treg: float
    T_reg_traffic: float
    Neutrophil_signature: float
    Granulocyte_traffic: float
    MDSC: float
    MDSC_traffic: float
    Macrophages: float
    Macrophage_DC_traffic: float
    Th2_signature: float
    Protumor_cytokines: float
    CAF: float
    Matrix: float
    Matrix_remodeling: float
    Angiogenesis: float
    Endothelium: float
    Proliferation_rate: float
    EMT_signature: float

    class Config:
        orm_mode = True


@app.get("/")
def show_signaturs_info(db: Session = Depends(get_db)):
    results = db.query(models.Signature).all()
    return results


@app.get("/{signatur_name}")
def show_signaturs_info(signatur_name: str, signature: Signature, db: Session = Depends(get_db)):

    signature_model = db.query(models.Signature).filter(models.Signature.NAME == signatur_name).first()

    return signature_model


@app.post("/")
def add_info(signature: Signature, db: Session = Depends(get_db)):

    signature_model = models.Signaturs()
    signature_model.NAME = signature.NAME
    signature_model.MHCI = signature.MHCI
    signature_model.MHCII = signature.MHCII
    signature_model.Coactivation_molecules = signature.Coactivation_molecules
    signature_model.Effector_cells = signature.Effector_cells
    signature_model.T_cell_traffic = signature.T_cell_traffic
    signature_model.NK_cells = signature.NK_cells
    signature_model.T_cells = signature.T_cells
    signature_model.B_cells = signature.B_cells
    signature_model.M1_signatures = signature.M1_signatures
    signature_model.Th1_signature = signature.Th1_signature
    signature_model.Antitumor_cytokines = signature.Antitumor_cytokines
    signature_model.Checkpoint_inhibition = signature.Checkpoint_inhibition
    signature_model.Treg = signature.Treg
    signature_model.T_reg_traffic = signature.T_reg_traffic
    signature_model.Neutrophil_signature = signature.Neutrophil_signature
    signature_model.Granulocyte_traffic = signature.Granulocyte_traffic
    signature_model.MDSC = signature.MDSC
    signature_model.MDSC_traffic = signature.MDSC_traffic
    signature_model.Macrophages = signature.Macrophages
    signature_model.Macrophage_DC_traffic = signature.Macrophage_DC_traffic
    signature_model.Th2_signature = signature.Th2_signature
    signature_model.Protumor_cytokines = signature.Protumor_cytokines
    signature_model.CAF = signature.CAF
    signature_model.Matrix = signature.Matrix
    signature_model.Matrix_remodeling = signature.Matrix_remodeling
    signature_model.Angiogenesis = signature.Angiogenesis
    signature_model.Endothelium = signature.Endothelium
    signature_model.Proliferation_rate = signature.Proliferation_rate
    signature_model.EMT_signature = signature.EMT_signature

    db.add(signature_model)
    db.commit()

    return signature


@app.put("/{signature_name}")
def update_info(signature_name: str, signature: Signature, db: Session = Depends(get_db)):

    signature_model = db.query(models.Signaturs).filter(models.Signaturs.NAME == signature_name).first()

    if signature_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {signature_name} : Does not exist"
        )

    signature_model.NAME = signature.NAME
    signature_model.MHCI = signature.MHCI
    signature_model.MHCII = signature.MHCII
    signature_model.Coactivation_molecules = signature.Coactivation_molecules
    signature_model.Effector_cells = signature.Effector_cells
    signature_model.T_cell_traffic = signature.T_cell_traffic
    signature_model.NK_cells = signature.NK_cells
    signature_model.T_cells = signature.T_cells
    signature_model.B_cells = signature.B_cells
    signature_model.M1_signatures = signature.M1_signatures
    signature_model.Th1_signature = signature.Th1_signature
    signature_model.Antitumor_cytokines = signature.Antitumor_cytokines
    signature_model.Checkpoint_inhibition = signature.Checkpoint_inhibition
    signature_model.Treg = signature.Treg
    signature_model.T_reg_traffic = signature.T_reg_traffic
    signature_model.Neutrophil_signature = signature.Neutrophil_signature
    signature_model.Granulocyte_traffic = signature.Granulocyte_traffic
    signature_model.MDSC = signature.MDSC
    signature_model.MDSC_traffic = signature.MDSC_traffic
    signature_model.Macrophages = signature.Macrophages
    signature_model.Macrophage_DC_traffic = signature.Macrophage_DC_traffic
    signature_model.Th2_signature = signature.Th2_signature
    signature_model.Protumor_cytokines = signature.Protumor_cytokines
    signature_model.CAF = signature.CAF
    signature_model.Matrix = signature.Matrix
    signature_model.Matrix_remodeling = signature.Matrix_remodeling
    signature_model.Angiogenesis = signature.Angiogenesis
    signature_model.Endothelium = signature.Endothelium
    signature_model.Proliferation_rate = signature.Proliferation_rate
    signature_model.EMT_signature = signature.EMT_signature

    db.add(signature_model)
    db.commit()

    return signature


@app.delete("/{signature_name}")
def delete_info(signature_name: str, db: Session = Depends(get_db)):

    signature_model = db.query(models.Signaturs).filter(models.Signaturs.NAME == signature_name).first()

    if signature_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {signature_name} : Does not exist"
        )

    db.query(models.Signaturs).filter(models.Signaturs.NAME == signature_name).delete()

    db.commit()