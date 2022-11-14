import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowPrdComponent } from './show-prd.component';

describe('ShowPrdComponent', () => {
  let component: ShowPrdComponent;
  let fixture: ComponentFixture<ShowPrdComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowPrdComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowPrdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
